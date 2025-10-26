import string
import nltk
from nltk.corpus import stopwords
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
import json

nltk.download('stopwords')

data = pd.read_csv('Emails.csv')

# Balanced sampling of the smaller class size
ham_msg = data[data['label'] == 'ham']
spam_msg = data[data['label'] == 'spam']

min_size = min(len(ham_msg), len(spam_msg))
ham_msg_balanced = ham_msg.sample(n=min_size, random_state=42)
spam_msg_balanced = spam_msg.sample(n=min_size, random_state=42)
balanced_data = pd.concat([ham_msg_balanced, spam_msg_balanced])

def remove_punctuations(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def remove_stopwords(text):
    stop_words = stopwords.words('english')
    return " ".join([w for w in text.split() if w.lower() not in stop_words])

balanced_data['text'] = balanced_data['text'].apply(remove_punctuations)
balanced_data['text'] = balanced_data['text'].apply(remove_stopwords)

train_X, test_X, train_Y, test_Y = train_test_split(
    balanced_data['text'],
    (balanced_data['label'] == 'spam').astype(int),
    test_size=0.2,
    random_state=42
)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_X)

with open('tokenizer.json', 'w') as f:
    f.write(tokenizer.to_json())

max_len = 100
train_seq = tokenizer.texts_to_sequences(train_X)
test_seq = tokenizer.texts_to_sequences(test_X)

train_pad = pad_sequences(train_seq, maxlen=max_len)
test_pad = pad_sequences(test_seq, maxlen=max_len)

model = Sequential([
    Embedding(len(tokenizer.word_index) + 1, 32, input_length=max_len),
    LSTM(16),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid'),
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_pad, train_Y, validation_data=(test_pad, test_Y), epochs=10, batch_size=32)

model.save('spam_detector.h5')
