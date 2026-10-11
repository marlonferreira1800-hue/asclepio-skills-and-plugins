import os
import markdown
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
import io

# Escopos necessários para ler/escrever no Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def get_google_drive_service():
    """Autentica o usuário e retorna o serviço do Google Drive API."""
    creds = None
    # Verifica se já temos o token salvo de um login anterior
    if os.path.exists('token.json'):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    # Se não temos credenciais válidas, pede para o usuário fazer login
    if not creds or not creds.valid:
        if not os.path.exists('credentials.json'):
            print("[ERRO] Arquivo credentials.json não encontrado!")
            print("Por favor, baixe o arquivo de credenciais do Google Cloud Console e coloque-o nesta pasta.")
            return None
            
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        
        # Salva as credenciais para a próxima vez
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

def publish_to_google_docs(draft_path):
    print(f"[Google Docs] Lendo o rascunho de: {draft_path}")
    
    if not os.path.exists(draft_path):
        print(f"[ERRO] Rascunho não encontrado em {draft_path}")
        return

    # Lê o Markdown
    with open(draft_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Converte para HTML (O Google Drive converte HTML perfeitamente para Google Docs)
    html_text = markdown.markdown(md_text)
    
    # Adiciona um estilo básico para garantir boa renderização
    html_content = f"<html><body>{html_text}</body></html>"
    
    service = get_google_drive_service()
    if not service:
        return

    print("[Google Docs] Fazendo upload e convertendo para Google Doc...")
    
    file_metadata = {
        'name': 'Rascunho: Newsletter Agentic',
        'mimeType': 'application/vnd.google-apps.document'
    }
    
    media = MediaIoBaseUpload(io.BytesIO(html_content.encode('utf-8')),
                              mimetype='text/html',
                              resumable=True)
                              
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id, webViewLink').execute()
                                  
    print("\n" + "="*50)
    print("✅ SUCESSO! O rascunho foi salvo no seu Google Docs.")
    print(f"🔗 LINK PARA ACESSAR: {file.get('webViewLink')}")
    print("="*50 + "\n")

if __name__ == '__main__':
    # Tenta encontrar o arquivo scratch/newsletter_draft.md a partir da raiz do projeto
    draft_path = os.path.join(os.path.dirname(__file__), '..', '..', 'scratch', 'newsletter_draft.md')
    publish_to_google_docs(draft_path)
