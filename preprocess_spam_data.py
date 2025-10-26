import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import nltk

nltk.download('stopwords')

df = pd.read_csv('spamhamdata.csv', sep='\t', header=None, names=['label', 'message'])

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\S+@\S+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    text = re.sub('\s+', ' ', text)
    return text

df['cleaned_message'] = df['message'].apply(clean_text)

stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

def preprocess_text(text):
    tokens = text.split()
    filtered_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

df['processed_message'] = df['cleaned_message'].apply(preprocess_text)

le = LabelEncoder()
df['label_enc'] = le.fit_transform(df['label'])

X_train, X_test, y_train, y_test = train_test_split(
    df['processed_message'], df['label_enc'], test_size=0.2, random_state=42)

df[['processed_message', 'label_enc']].to_csv('Emails.csv', index=False)
