"""Inserir no seu aplicativo APÓS a chamada real, usando resposta final."""
import importlib.util
from datetime import datetime, timezone
from pathlib import Path
script = Path(__file__).resolve().parents[1] / 'skills/medir-tokens/scripts/tokenmeter.py'
spec = importlib.util.spec_from_file_location('tokenmeter', script)
tokenmeter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tokenmeter)

def registrar_resposta(response_dict, provider, platform, account, request_id=None):
    envelope = {'provider':provider, 'platform':platform, 'account':account,
                'timestamp':datetime.now(timezone.utc).isoformat(), 'response':response_dict}
    if request_id is not None: envelope['id'] = request_id
    ledger = tokenmeter.Ledger()
    try: return ledger.add_many([envelope])
    finally: ledger.db.close()

# Exemplo na sua aplicação:
# response = client.responses.create(...)  # chamada real feita por você
# registrar_resposta(response.model_dump(), 'openai', 'meu-app', 'meu-projeto')
# Para outro SDK, converter a resposta final para dict e usar provider correspondente.
# Não registrar cada chunk: usar uma vez os metadados finais completos.
