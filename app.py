from gmail_auth import get_service, fetch_emails
from preprocess import preprocess_text, extract_email_text, get_decoded_subject
from model import load_model, predict_spam

def main():
    service = get_service()
    emails = fetch_emails(service, max_results=20)
    model, vectorizer = load_model()

    for email_obj in emails:
        mime_msg = email_obj['message']

        subject = get_decoded_subject(mime_msg)
        email_text = extract_email_text(mime_msg)
        processed_text = preprocess_text(email_text)
        prediction = predict_spam(model, vectorizer, processed_text)
        print(f"Email ID: {email_obj['id']}")
        print(f"Subject: {subject}")
        print(f"Spam: {'Yes' if prediction == 1 else 'No'}")
        print('-' * 40)

if __name__ == '__main__':
    main()
