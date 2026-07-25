# ============================================================
#  Phishing Detection — NLP & Machine Learning
#  Author : Shyam Ravi
#  Description: Detects phishing messages using TF-IDF
#               vectorization and Logistic Regression
#  Dataset: Auto-downloaded SMS Spam Collection Dataset
# ============================================================

import os
import sys
import io
import pandas as pd
import nltk
import re
import pickle
import urllib.request
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Fix Windows encoding issue
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Download required NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# ─────────────────────────────────────
#  PATHS
# ─────────────────────────────────────
DATASET_URL     = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
DATASET_PATH    = "data/sms.tsv"
MODEL_PATH      = "model/phishing_model.pkl"
VECTORIZER_PATH = "model/tfidf_vectorizer.pkl"
RESULTS_PATH    = "results/predictions.txt"

# ─────────────────────────────────────
#  CREATE FOLDERS
# ─────────────────────────────────────
os.makedirs('data',    exist_ok=True)
os.makedirs('model',   exist_ok=True)
os.makedirs('results', exist_ok=True)


# ─────────────────────────────────────
#  AUTO DOWNLOAD DATASET
# ─────────────────────────────────────
def download_dataset():
    if not os.path.exists(DATASET_PATH):
        print("[*] Dataset not found -- downloading automatically...")
        urllib.request.urlretrieve(DATASET_URL, DATASET_PATH)
        print("[+] Dataset downloaded successfully!")
    else:
        print("[+] Dataset already exists -- skipping download!")


# ─────────────────────────────────────
#  RULE-BASED KEYWORD FILTER
# ─────────────────────────────────────
PHISHING_KEYWORDS = [
    "verify your account", "click here", "urgent", "suspended",
    "confirm your details", "login immediately", "unusual activity",
    "your account has been", "limited time", "act now", "prize",
    "you have won", "free gift", "reset your password", "validate",
    "update your billing", "congratulations", "selected", "winner"
]

def keyword_check(text):
    text_lower = text.lower()
    for keyword in PHISHING_KEYWORDS:
        if keyword in text_lower:
            return True
    return False


# ─────────────────────────────────────
#  TEXT PREPROCESSING
# ─────────────────────────────────────
stemmer    = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text   = text.lower()
    text   = re.sub(r'http\S+|www\S+', '', text)
    text   = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()
    tokens = [stemmer.stem(t) for t in tokens if t not in stop_words]
    return ' '.join(tokens)


# ─────────────────────────────────────
#  TRAIN & SAVE MODEL
# ─────────────────────────────────────
def train_and_save_model():
    print("[*] Loading dataset...")
    df = pd.read_csv(
        DATASET_PATH, sep='\t',
        header=None, names=['label', 'message'],
        encoding='latin-1'
    )
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    print("[*] Preprocessing text...")
    df['clean_message'] = df['message'].apply(preprocess)

    X_train, X_test, y_train, y_test = train_test_split(
        df['clean_message'], df['label'],
        test_size=0.2, random_state=42
    )

    print("[*] Vectorizing with TF-IDF...")
    vectorizer      = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_train_tfidf   = vectorizer.fit_transform(X_train)
    X_test_tfidf    = vectorizer.transform(X_test)

    print("[*] Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)

    y_pred   = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n[+] Accuracy: {accuracy:.4f}")
    print("\n[+] Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Legitimate', 'Phishing']))

    print("[*] Saving model...")
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    with open(VECTORIZER_PATH, 'wb') as f:
        pickle.dump(vectorizer, f)
    print("[+] Model saved to model/phishing_model.pkl")
    print("[+] Vectorizer saved to model/tfidf_vectorizer.pkl")

    return model, vectorizer


# ─────────────────────────────────────
#  LOAD SAVED MODEL
# ─────────────────────────────────────
def load_model():
    print("[+] Saved model found -- loading instantly!")
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer


# ─────────────────────────────────────
#  PREDICTION
# ─────────────────────────────────────
def predict(text, model, vectorizer):
    if keyword_check(text):
        return u"\u26a0\ufe0f  PHISHING DETECTED (keyword match)"
    clean       = preprocess(text)
    vector      = vectorizer.transform([clean])
    prediction  = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0][1]
    if prediction == 1:
        return u"\u26a0\ufe0f  PHISHING DETECTED (confidence: {:.2%})".format(probability)
    else:
        return u"\u2705 LEGITIMATE (confidence: {:.2%})".format(1 - probability)


# ─────────────────────────────────────
#  SAVE RESULTS
# ─────────────────────────────────────
def save_results(test_messages, model, vectorizer):
    with open(RESULTS_PATH, 'w', encoding='utf-8') as f:
        f.write("=" * 55 + "\n")
        f.write("  Phishing Detection Results -- Shyam Ravi\n")
        f.write("=" * 55 + "\n\n")
        for msg in test_messages:
            result = predict(msg, model, vectorizer)
            f.write(f"Message : {msg}\n")
            f.write(f"Result  : {result}\n")
            f.write("-" * 55 + "\n")
    print(f"[+] Results saved to {RESULTS_PATH}")


# ─────────────────────────────────────
#  MAIN
# ─────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("   Phishing Detection System -- Shyam Ravi")
    print("=" * 55 + "\n")

    download_dataset()

    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model, vectorizer = load_model()
    else:
        model, vectorizer = train_and_save_model()

    test_messages = [
        "Congratulations! You have won a free iPhone. Click here to claim your prize now!",
        "Hi, are we still meeting tomorrow at 3pm for the project review?",
        "URGENT: Your bank account has been suspended. Verify your details immediately.",
        "Hey, just checking if you received the document I sent yesterday.",
        "Your password needs to be reset. Login immediately to secure your account."
    ]

    print("\n" + "=" * 55)
    print("   Sample Predictions")
    print("=" * 55)
    for msg in test_messages:
        result = predict(msg, model, vectorizer)
        print(f"\nMessage : {msg[:60]}...")
        print(f"Result  : {result}")

    save_results(test_messages, model, vectorizer)