import os.path
import base64
import email
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)  # Changed from port=0 to port=8080
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def fetch_emails(service, max_results=10):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    emails = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        msg_raw = base64.urlsafe_b64decode(msg_data['raw'].encode('ASCII'))
        mime_msg = email.message_from_bytes(msg_raw)
        emails.append({'id': msg['id'], 'message': mime_msg})
    return emails

def get_service():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials=creds)
    return service
