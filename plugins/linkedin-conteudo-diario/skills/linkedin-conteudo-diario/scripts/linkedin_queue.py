"""Create and track a local LinkedIn content queue.

This utility performs local file operations only. It does not access LinkedIn,
store credentials, generate content, or make network requests.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date as date_type
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


VALID_STATUSES = {
    "planned",
    "prepared",
    "approved",
    "scheduled",
    "published",
    "failed",
}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def fail(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    raise SystemExit(1)


def write_json(data: object, output_file: str) -> None:
    path = Path(output_file).expanduser().resolve()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    except (OSError, TypeError) as exc:
        fail(f"cannot write {path}: {exc}")
    print(f"Success! Data written to: {path}")


def read_json(input_file: str) -> dict:
    path = Path(input_file).expanduser().resolve()
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path}: {exc}")
    if not isinstance(data, dict):
        fail(f"expected a JSON object in {path}")
    return data


def parse_date(value: str) -> date_type:
    try:
        return date_type.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("date must use YYYY-MM-DD") from exc


def parse_csv(value: str, label: str) -> list[str]:
    items = [item.strip() for item in value.split(",") if item.strip()]
    if not items:
        raise argparse.ArgumentTypeError(f"{label} must not be empty")
    return items


def validate_time(value: str) -> str:
    if not re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d", value):
        raise argparse.ArgumentTypeError(f"invalid time {value!r}; use HH:MM")
    return value


def resolve_timezone(value: str):
    """Resolve an IANA timezone with a dependency-free Brasilia fallback."""
    try:
        return ZoneInfo(value)
    except ZoneInfoNotFoundError:
        if value == "America/Sao_Paulo":
            # Brazil has observed UTC-03:00 year-round since 2019. This explicit
            # fallback keeps the skill usable on Windows Python installations
            # that do not bundle the IANA tzdata package.
            return timezone(timedelta(hours=-3), name="America/Sao_Paulo")
        raise


def command_plan(args: argparse.Namespace) -> None:
    if args.quantity < 1:
        fail("quantity must be at least 1")

    topics = parse_csv(args.topics, "topics")
    times = [validate_time(value) for value in parse_csv(args.times, "times")]
    if len(times) != args.quantity:
        fail(
            f"quantity is {args.quantity}, but {len(times)} publication times "
            "were supplied"
        )
    if len(set(times)) != len(times):
        fail("publication times must be unique")

    try:
        zone = resolve_timezone(args.timezone)
    except ZoneInfoNotFoundError as exc:
        fail(f"unknown timezone {args.timezone!r}: {exc}")

    target_date = args.date
    assets_dir = Path(args.assets_dir).expanduser().resolve()
    posts_dir = assets_dir / "posts"
    images_dir = assets_dir / "images"
    posts_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    items = []
    for index in range(args.quantity):
        number = index + 1
        topic = topics[index % len(topics)]
        local_dt = datetime.fromisoformat(
            f"{target_date.isoformat()}T{times[index]}:00"
        ).replace(tzinfo=zone)
        items.append(
            {
                "id": f"post-{number:02d}",
                "topic": topic,
                "scheduled_local": local_dt.isoformat(),
                "timezone": args.timezone,
                "post_file": str(posts_dir / f"{number:02d}.md"),
                "image_file": str(images_dir / f"{number:02d}.png"),
                "status": "planned",
                "attempts": 0,
                "external_id": None,
                "url": None,
                "error": None,
            }
        )

    queue = {
        "schema_version": 1,
        "created_at": datetime.now(zone).isoformat(),
        "date": target_date.isoformat(),
        "timezone": args.timezone,
        "quantity": args.quantity,
        "approval": {"status": "pending", "approved_at": None},
        "items": items,
    }
    write_json(queue, args.output)


def validate_queue(queue: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    items = queue.get("items")
    quantity = queue.get("quantity")

    if not isinstance(items, list):
        return {"valid": False, "errors": ["items must be a list"], "warnings": []}
    if quantity != len(items):
        errors.append(f"quantity is {quantity!r}, but queue contains {len(items)} items")

    ids: list[str] = []
    topics: list[str] = []
    times: list[str] = []
    for item in items:
        if not isinstance(item, dict):
            errors.append("every queue item must be an object")
            continue
        item_id = str(item.get("id", ""))
        ids.append(item_id)
        topics.append(str(item.get("topic", "")))
        times.append(str(item.get("scheduled_local", "")))

        status = item.get("status")
        if status not in VALID_STATUSES:
            errors.append(f"{item_id or '<missing id>'}: invalid status {status!r}")

        post_file = Path(str(item.get("post_file", "")))
        image_file = Path(str(item.get("image_file", "")))
        if not post_file.is_file() or post_file.stat().st_size == 0:
            errors.append(f"{item_id}: missing or empty post file: {post_file}")
        else:
            text = post_file.read_text(encoding="utf-8").strip()
            if len(text) < 80:
                warnings.append(f"{item_id}: post is unusually short ({len(text)} chars)")
            if not re.search(r"#[\wÀ-ÿ]+", text):
                warnings.append(f"{item_id}: post has no hashtag")

        if not image_file.is_file() or image_file.stat().st_size == 0:
            errors.append(f"{item_id}: missing or empty image file: {image_file}")
        elif image_file.suffix.lower() not in IMAGE_EXTENSIONS:
            errors.append(f"{item_id}: unsupported image extension: {image_file.suffix}")

    for label, values in (("id", ids), ("scheduled time", times)):
        duplicates = [value for value, count in Counter(values).items() if count > 1]
        if duplicates:
            errors.append(f"duplicate {label} values: {duplicates}")
    duplicate_topics = [value for value, count in Counter(topics).items() if count > 1]
    if duplicate_topics:
        warnings.append(f"repeated topics in the same batch: {duplicate_topics}")

    return {
        "valid": not errors,
        "checked_items": len(items),
        "errors": errors,
        "warnings": warnings,
    }


def command_validate(args: argparse.Namespace) -> None:
    queue = read_json(args.queue)
    write_json(validate_queue(queue), args.output)


def command_status(args: argparse.Namespace) -> None:
    queue = read_json(args.queue)
    items = queue.get("items", [])
    counts = Counter(
        item.get("status", "invalid") for item in items if isinstance(item, dict)
    )
    summary = {
        "date": queue.get("date"),
        "timezone": queue.get("timezone"),
        "approval": queue.get("approval"),
        "total": len(items),
        "by_status": dict(sorted(counts.items())),
        "items": [
            {
                "id": item.get("id"),
                "topic": item.get("topic"),
                "scheduled_local": item.get("scheduled_local"),
                "status": item.get("status"),
                "url": item.get("url"),
                "error": item.get("error"),
            }
            for item in items
            if isinstance(item, dict)
        ],
    }
    write_json(summary, args.output)


def command_record(args: argparse.Namespace) -> None:
    queue = read_json(args.queue)
    items = queue.get("items")
    if not isinstance(items, list):
        fail("queue items must be a list")

    matches = [item for item in items if item.get("id") == args.item_id]
    if len(matches) != 1:
        fail(f"expected one item with id {args.item_id!r}, found {len(matches)}")

    item = matches[0]
    item["status"] = args.status
    item["attempts"] = int(item.get("attempts", 0)) + 1
    item["external_id"] = args.external_id
    item["url"] = args.url
    item["error"] = args.error
    item["updated_at"] = datetime.now().astimezone().isoformat()

    if args.status == "approved":
        queue["approval"] = {
            "status": "approved",
            "approved_at": datetime.now().astimezone().isoformat(),
        }

    write_json(queue, args.output)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create, validate, and track a local LinkedIn content queue."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan = subparsers.add_parser("plan", help="Create a new publication queue")
    plan.add_argument("--date", type=parse_date, required=True)
    plan.add_argument("--timezone", required=True)
    plan.add_argument("--quantity", type=int, required=True)
    plan.add_argument("--times", required=True, help="Comma-separated HH:MM values")
    plan.add_argument("--topics", required=True, help="Comma-separated topics")
    plan.add_argument("--assets-dir", required=True)
    plan.add_argument("--output", required=True)

    validate = subparsers.add_parser("validate", help="Validate queue files")
    validate.add_argument("--queue", required=True)
    validate.add_argument("--output", required=True)

    status = subparsers.add_parser("status", help="Summarize queue status")
    status.add_argument("--queue", required=True)
    status.add_argument("--output", required=True)

    record = subparsers.add_parser("record", help="Record an item result")
    record.add_argument("--queue", required=True)
    record.add_argument("--item-id", required=True)
    record.add_argument("--status", choices=sorted(VALID_STATUSES), required=True)
    record.add_argument("--external-id")
    record.add_argument("--url")
    record.add_argument("--error")
    record.add_argument("--output", required=True)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "plan":
            command_plan(args)
        elif args.command == "validate":
            command_validate(args)
        elif args.command == "status":
            command_status(args)
        elif args.command == "record":
            command_record(args)
        else:
            fail(f"unknown command: {args.command}")
    except (OSError, ValueError, UnicodeError) as exc:
        fail(str(exc))


if __name__ == "__main__":
    main()

