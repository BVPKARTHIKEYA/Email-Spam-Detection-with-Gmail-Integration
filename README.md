Gmail Spam Guard Pro 📧
A machine learning project for advanced email spam detection, integrating natural language processing techniques and Gmail API. Gmail Spam Guard Pro can preprocess large volumes of email, train robust models, and classify messages automatically, making your inbox safer and cleaner. It's fully compatible with Gmail using Google's official API, all in Python.

📋 Table of Contents
Features

Project Structure

Technologies Used

Installation

Configuration

Usage

Model Training

Contributing

License

Author

Acknowledgments

✨ Features
ML-Based Spam Detection: Classifies emails as spam or not spam with high accuracy

Gmail API Integration: Fetch and classify live Gmail messages

Easy Setup: Fast configuration for any user with Google API credentials

End-to-End Pipeline: Preprocessing, model training, and inference included

Flexible ML Support: Compatible with both classic ML (Naive Bayes, SVM) and deep learning (LSTM, CNN)

Data Security: Never uploads your emails; operates locally after API access

Extensible: Easily add features, change models, or expand datasets

📁 Project Structure
text
Gmail-Spam-Guard-Pro/
├── .venv/                          # Python virtual environment
├── __pycache__/                    # Python cache files
├── .idea/                          # IDE configuration files
├── venv/                           # Alternate virtual environment
│
├── credentials.json                # Gmail API credentials
├── token.json                      # OAuth2 token for Gmail
├── tokenizer.json                  # Tokenizer configuration
│
├── Emails.csv                      # Gmail message dataset
├── spamhamdata.csv                 # Labeled dataset for training
│
├── model.py                        # Model architecture definition
├── train_model.py                  # Model training script
├── spam_detector.py                # Inference logic for spam detection
├── predict_spam.py                 # CLI/script for running predictions
│
├── preprocess.py                   # Data/text preprocessing utilities
├── preprocess_spam_data.py         # Extra preprocessing for spam data
│
├── gmail_auth.py                   # Handles Gmail authentication (OAuth)
├── read_gmail_and_detect_spam.py   # Fetches and classifies Gmail messages
├── generate_dataset.py             # Tool to create/generate datasets
│
├── spam_detector.h5                # Trained Keras deep learning model
├── spam_model.pkl                  # Pickled ML model
├── vectorizer.pkl                  # Persistence for vectorizer
├── requirements.txt                # Python dependency list
├── Dockerfile                      # For running in Docker
└── .gitignore                      # Ensures secrets are never committed
🛠️ Technologies Used
Python 3.8+

TensorFlow / Keras: For deep learning models

scikit-learn: Classic ML and utilities

pandas / numpy: Data handling

NLTK / spaCy: NLP and preprocessing

Gmail API (Google APIs Client): Secure email fetching

pickle / joblib: Model serialization

Docker: (Optional) Containerized and cross-platform

🚀 Installation
Clone the repository:

bash
git clone https://github.com/yourusername/gmail-spam-guard-pro.git
cd gmail-spam-guard-pro
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
⚙️ Configuration
Gmail API Setup
Go to the Google Cloud Console

Start a new project or select one

Enable Gmail API

Create OAuth2 credentials (Desktop app)

Download and save as credentials.json in your project root

Authenticate by running:

bash
python gmail_auth.py
Complete consent in your browser. token.json will be created

💻 Usage
1. Training Your Model
bash
python train_model.py
Loads spamhamdata.csv

Preprocesses text

Trains and saves a model (spam_model.pkl, spam_detector.h5)

Saves the vectorizer: vectorizer.pkl

2. Preprocessing Data
bash
python preprocess_spam_data.py
3. Fetch and Classify Live Gmail Emails
bash
python read_gmail_and_detect_spam.py
Authenticates with Gmail API

Downloads inbox emails

Predicts spam/not spam for each

Saves results in Emails.csv

4. Predict with the Trained Model
bash
python predict_spam.py
Or programmatically:

python
from predict_spam import predict_spam
result = predict_spam("Example email text")
print(result)
5. Generate Your Own Dataset
bash
python generate_dataset.py
📝 Data Formats
Train Data: spamhamdata.csv

text
label,text
spam,"Win a million now!"
ham,"Let's catch up next week."
Classified Gmail Data: Emails.csv

text
subject,sender,body,prediction,confidence
"You've won!","spam@scam.com","Click to claim",spam,0.98
"Status Update","teammate@company.com","Details attached",ham,0.94
🐳 Docker Deployment
Build the Docker image:

bash
docker build -t gmail-spam-guard-pro .
Run in Docker:

bash
docker run -it gmail-spam-guard-pro python read_gmail_and_detect_spam.py
📊 Typical Model Metrics
Accuracy: 95-98%

Precision: High (minimize false positives)

Recall: High (catch all spam)

F1 Score: Balanced and reliable

🤝 Contributing
Contributions, bug reports, and suggestions are welcome!

Fork this repository

Create a feature branch (git checkout -b feature/new-idea)

Make your change(s), test well

Commit (git commit -m 'My new idea')

Push (git push origin feature/new-idea)

Open a Pull Request

Direct Contribution Ideas
Improve spam/ham classification accuracy

Expand to multiple languages

Add phishing/scam detection

Build more dataset tools

Add explainability (LIME/SHAP)

UI/Web dashboard (future)

📄 License
MIT License. See the LICENSE file for details.

👤 Author
Karthikeya Boddeda

Email: sunny.penny041@gmail.com

GitHub: @yourusername

🙏 Acknowledgments
Google/Gmail API documentation

TensorFlow, scikit-learn, and open-source contributors

Community dataset creators

⚠️ Notes
Never commit your credentials.json, token.json, or actual inbox data

Respect Gmail's rate limits and privacy guidelines

All data remains local unless you change the code

⭐ If Gmail Spam Guard Pro helped protect your inbox, please star this repository!
# Live Demo

![a7dc645d-fcf8-4277-8214-14098a05872d](https://github.com/user-attachments/assets/d1464df9-d643-4002-8f1a-808ec0c9b708)
