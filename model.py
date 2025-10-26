from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train_model(texts, labels):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    model = LogisticRegression()
    model.fit(X, labels)
    # Save model and vectorizer
    joblib.dump(model, 'spam_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')

def load_model():
    import joblib
    model = joblib.load('spam_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    return model, vectorizer

def predict_spam(model, vectorizer, text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
