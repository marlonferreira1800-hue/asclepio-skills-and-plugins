import json, sys
from pathlib import Path

def render(source, target):
    data=json.loads(Path(source).read_text(encoding="utf-8"))
    if not isinstance(data.get("title"),str) or not isinstance(data.get("scenes"),list) or not data["scenes"]:
        raise ValueError("Roteiro precisa de title e scenes não vazias")
    for s in data["scenes"]:
        if not all(isinstance(s.get(k),str) for k in ("title","explanation","source")):
            raise ValueError("Cena sem título, explicação ou fonte")
        if not isinstance(s.get("steps"),list) or not 1 <= len(s["steps"]) <= 6 or not all(isinstance(v,str) for v in s["steps"]):
            raise ValueError("Cada cena precisa de 1–6 etapas textuais")
    payload=json.dumps(data,ensure_ascii=False).replace("<","\\u003c").replace(">","\\u003e").replace("&","\\u0026")
    template=(Path(__file__).resolve().parents[1]/"assets/player.html").read_text()
    Path(target).write_text(template.replace("__DATA__",payload),encoding="utf-8")

if __name__=="__main__":
    if len(sys.argv)!=3: raise SystemExit("Uso: render.py roteiro.json aula.html")
    render(sys.argv[1],sys.argv[2])
