import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from email.header import decode_header

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    text = re.sub(r'\W', ' ', text)
    text = text.lower()
    tokens = text.split()
    filtered_tokens = [ps.stem(w) for w in tokens if w not in stop_words]
    return ' '.join(filtered_tokens)

def decode_mime_words(s):
    """Decode encoded words in email headers to a readable string."""
    decoded_fragments = decode_header(s)
    decoded_string = ''
    for fragment, encoding in decoded_fragments:
        if isinstance(fragment, bytes):
            try:
                decoded_string += fragment.decode(encoding or 'utf-8', errors='ignore')
            except LookupError:
                decoded_string += fragment.decode('utf-8', errors='ignore')
        else:
            decoded_string += fragment
    return decoded_string

def get_decoded_subject(mime_msg):
    raw_subj = mime_msg['subject']
    if raw_subj:
        return decode_mime_words(raw_subj)
    return ''

def extract_email_text(mime_msg):
    """Extract full text (decoded subject + body) from the MIME message."""
    subject = get_decoded_subject(mime_msg)
    body = ''
    if mime_msg.is_multipart():
        for part in mime_msg.walk():
            if part.get_content_type() == 'text/plain':
                try:
                    body = part.get_payload(decode=True).decode(errors='ignore')
                except:
                    body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                break
    else:
        try:
            body = mime_msg.get_payload(decode=True).decode(errors='ignore')
        except:
            body = mime_msg.get_payload(decode=True).decode('utf-8', errors='ignore')
    return subject + ' ' + body
