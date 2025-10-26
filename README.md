# Gmail Spam Guard Pro 📧

<div align="center">

**Advanced ML-powered email spam detection with Gmail API integration**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Gmail API](https://img.shields.io/badge/Gmail-API-red.svg)](https://developers.google.com/gmail/api)

</div>

---

## 📖 Overview

Gmail Spam Guard Pro is a machine learning project that brings advanced spam detection to your Gmail inbox. Using natural language processing and the official Gmail API, it preprocesses emails, trains robust models, and automatically classifies messages—keeping your inbox safe and organized. All processing happens locally in Python, ensuring your data stays private.

## ✨ Features

- 🤖 **ML-Based Detection** - High-accuracy spam classification using state-of-the-art algorithms
- 📬 **Gmail Integration** - Seamless fetching and classification of live Gmail messages
- ⚡ **Quick Setup** - Fast configuration with Google API credentials
- 🔄 **Complete Pipeline** - End-to-end preprocessing, training, and inference
- 🧠 **Flexible Models** - Support for classic ML (Naive Bayes, SVM) and deep learning (LSTM, CNN)
- 🔒 **Privacy First** - All operations run locally; emails never leave your machine
- 🔧 **Extensible** - Easy to customize models, features, and datasets

## 🎬 Live Demo

![Gmail Spam Guard Pro Demo](https://github.com/user-attachments/assets/d1464df9-d643-4002-8f1a-808ec0c9b708)

---

## 📁 Project Structure

```
Gmail-Spam-Guard-Pro/
├── .venv/                          # Python virtual environment
├── __pycache__/                    # Python cache files
├── .idea/                          # IDE configuration files
├── venv/                           # Alternate virtual environment
│
├── credentials.json                # Gmail API credentials (DO NOT COMMIT)
├── token.json                      # OAuth2 token for Gmail (DO NOT COMMIT)
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
│
├── requirements.txt                # Python dependency list
├── Dockerfile                      # Docker configuration
├── .gitignore                      # Git ignore file
└── README.md                       # Project documentation
```

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.8+ |
| **Deep Learning** | TensorFlow, Keras |
| **Machine Learning** | scikit-learn |
| **Data Processing** | pandas, numpy |
| **NLP** | NLTK, spaCy |
| **API** | Gmail API (Google APIs Client) |
| **Serialization** | pickle, joblib |
| **Containerization** | Docker (Optional) |

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Cloud account (for Gmail API)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/gmail-spam-guard-pro.git
   cd gmail-spam-guard-pro
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate (Linux/Mac)
   source venv/bin/activate
   
   # Activate (Windows)
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration

### Gmail API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Gmail API** for your project
4. Create **OAuth2 credentials** (Desktop application type)
5. Download the credentials and save as `credentials.json` in the project root
6. Run the authentication script:
   ```bash
   python gmail_auth.py
   ```
7. Complete the OAuth consent flow in your browser
8. A `token.json` file will be automatically created

> ⚠️ **Security Note**: Never commit `credentials.json` or `token.json` to version control!

---

## 💻 Usage

### 1. Training Your Model

Train the spam detection model on your dataset:

```bash
python train_model.py
```

This script will:
- Load `spamhamdata.csv`
- Preprocess the text data
- Train and evaluate the model
- Save the trained model (`spam_model.pkl`, `spam_detector.h5`)
- Save the vectorizer (`vectorizer.pkl`)

### 2. Preprocessing Data

Prepare and clean your spam dataset:

```bash
python preprocess_spam_data.py
```

### 3. Fetch and Classify Gmail Emails

Automatically fetch and classify emails from your Gmail inbox:

```bash
python read_gmail_and_detect_spam.py
```

This will:
- Authenticate with the Gmail API
- Download emails from your inbox
- Predict spam/ham for each message
- Save results to `Emails.csv`

### 4. Predict Individual Emails

Run predictions on custom text:

```bash
python predict_spam.py
```

Or use programmatically:

```python
from predict_spam import predict_spam

result = predict_spam("Congratulations! You've won a million dollars!")
print(result)  # Output: spam
```

### 5. Generate Custom Datasets

Create your own training dataset:

```bash
python generate_dataset.py
```

---

## 📝 Data Formats

### Training Data (`spamhamdata.csv`)

```csv
label,text
spam,"Win a million dollars now! Click here!"
ham,"Hi, let's catch up next week for coffee."
spam,"URGENT: Your account has been suspended"
ham,"Meeting notes attached from today's standup"
```

### Classified Gmail Data (`Emails.csv`)

```csv
subject,sender,body,prediction,confidence
"You've won!","spam@scam.com","Click to claim your prize",spam,0.98
"Weekly Update","teammate@company.com","Project status attached",ham,0.94
"Verify Account","phish@fake.com","Confirm your details now",spam,0.96
```

---

## 🐳 Docker Deployment

### Build the Docker Image

```bash
docker build -t gmail-spam-guard-pro .
```

### Run in Docker

```bash
docker run -it gmail-spam-guard-pro python read_gmail_and_detect_spam.py
```

---

## 📊 Model Performance

Typical metrics achieved with Gmail Spam Guard Pro:

| Metric | Score |
|--------|-------|
| **Accuracy** | 95-98% |
| **Precision** | High (minimizes false positives) |
| **Recall** | High (catches all spam) |
| **F1 Score** | Balanced and reliable |

---

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome!

### How to Contribute

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes and test thoroughly
4. **Commit** your changes (`git commit -m 'Add amazing feature'`)
5. **Push** to the branch (`git push origin feature/amazing-feature`)
6. **Open** a Pull Request

### Contribution Ideas

- 🎯 Improve spam/ham classification accuracy
- 🌍 Expand to multiple languages
- 🎣 Add phishing/scam detection
- 📊 Build more dataset generation tools
- 🔍 Add model explainability (LIME/SHAP)
- 🖥️ Create a web dashboard UI
- 📱 Mobile app integration

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Karthikeya Boddeda**

- 📧 Email: sunny.penny041@gmail.com
- 💻 GitHub: [@BVPKARTHIKEYA](https://github.com/BVPKARTHIKEYA)

---

## 🙏 Acknowledgments

- Google/Gmail API [documentation](https://developers.google.com/gmail/api)
- TensorFlow and scikit-learn communities
- Open-source contributors and dataset creators
- The amazing Python community

---

## ⚠️ Important Notes

- 🔐 **Never commit** `credentials.json`, `token.json`, or actual inbox data to version control
- 📊 Respect Gmail's API rate limits and privacy guidelines
- 💾 All data remains local unless you explicitly modify the code
- 🔒 This tool processes emails locally for maximum privacy

---

## 🌟 Support

If Gmail Spam Guard Pro helped protect your inbox, please consider:

- ⭐ Starring this repository
- 🐛 Reporting bugs or issues
- 💡 Suggesting new features
- 🤝 Contributing code improvements

---

<div align="center">

**Made with ❤️ by Karthikeya Boddeda**

</div>
