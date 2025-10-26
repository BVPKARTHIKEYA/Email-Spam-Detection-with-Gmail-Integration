import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'       # Suppresses INFO, WARNING, and ERROR logs except fatal ones
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'      # Disables oneDNN optimizations messages

import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json

# Load the trained spam detection model
model = load_model('spam_detector.h5')

# Load the tokenizer from JSON string (read as string, not dict)
with open('tokenizer.json') as f:
    tokenizer = tokenizer_from_json(f.read())

max_len = 100  # max sequence length used during training

def predict_spam(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=max_len)
    pred = model.predict(padded)[0][0]
    return "Spam" if pred > 0.5 else "Not Spam"

if __name__ == "__main__":
    email_text = input("Enter email text to classify: ")
    result = predict_spam(email_text)
    print(f"Classification: {result}")
