import os.path
import base64
import json
import tensorflow as tf
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import tokenizer_from_json

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

model = load_model('spam_detector.h5')
with open('tokenizer.json') as f:
    tokenizer = tokenizer_from_json(json.load(f))
max_len = 100

def predict_spam(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)
    pred = model.predict(padded)[0][0]
    return "Spam" if pred > 0.5 else "Not Spam"

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])

    if not messages:
        print("No unread emails found.")
        return

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg.get('payload', {})
        parts = payload.get('parts', [])
        body = ""

        if 'body' in payload and payload['body'].get('data'):
            data = payload['body']['data']
            body = base64.urlsafe_b64decode(data).decode('utf-8')
        else:
            for part in parts:
                if part.get('mimeType') == 'text/plain':
                    data = part['body'].get('data')
                    if data:
                        body = base64.urlsafe_b64decode(data).decode('utf-8')
                        break

        print(f"Email snippet:\n{body[:200]}...\n")
        result = predict_spam(body)
        print(f"Spam Detection Result: {result}\n")

        service.users().messages().modify(
            userId='me',
            id=message['id'],
            body={'removeLabelIds': ['UNREAD']}
        ).execute()

if __name__ == '__main__':
    main()
