# 🎣 Phishing Detection — NLP & Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python&logoColor=white)
![ML](https://img.shields.io/badge/ML-Logistic%20Regression-orange?style=flat)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20NLTK-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

> A machine learning system that detects phishing messages using Natural Language Processing — classifying text as spam or legitimate using TF-IDF vectorization and Logistic Regression.

---

## 📌 Objective

Build a phishing detection pipeline that preprocesses raw text messages, extracts meaningful features using NLP techniques, and classifies them as phishing or legitimate using a trained machine learning model.

---

## 🧠 How It Works

```
Raw Text Message
      │
      ▼
Text Preprocessing (NLTK)
 - Lowercase conversion
 - Remove punctuation & stopwords
 - Tokenization & stemming
      │
      ▼
Feature Extraction (TF-IDF)
 - Converts text to numerical vectors
 - Weights rare but important words higher
      │
      ▼
Rule-Based Keyword Filter
 - Flags known phishing keywords
 - (e.g. "verify account", "click here", "urgent")
      │
      ▼
Logistic Regression Model (scikit-learn)
 - Trained on labeled spam/ham dataset
 - Predicts: Phishing ⚠️ or Legitimate ✅
      │
      ▼
Classification Result
```

---

## 🛠️ Tech Stack

| Component | Tool / Library |
|---|---|
| Language | Python 3.x |
| Text Preprocessing | NLTK |
| Data Handling | Pandas |
| Feature Extraction | TF-IDF (scikit-learn) |
| ML Model | Logistic Regression (scikit-learn) |
| Keyword Analysis | Rule-based (custom) |

---

## 📁 Project Structure

```
Phishing-Detection-NLP/
│
├── README.md
├── phishing_detector.py       ← main detection script
├── train_model.py             ← model training script
├── requirements.txt           ← dependencies
│
├── data/
│   └── dataset.csv            ← labeled spam/ham dataset
│
├── model/
│   └── model_notes.md         ← model details & observations
│
└── results/
    └── results_notes.md       ← sample outputs & findings
```

---

## ⚙️ Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/Phishing-Detection-NLP.git
cd Phishing-Detection-NLP
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the detector
```bash
python phishing_detector.py
```

---

## 🔍 Key Features

- Text cleaned and normalized using NLTK pipelines
- TF-IDF vectorization to capture word importance across messages
- Rule-based keyword filter as a first-pass detection layer
- Logistic Regression model trained on real spam/ham dataset
- Easy to extend with new keywords or swap in a different ML model

---

## 🗺️ MITRE ATT&CK Relevance

| Technique | ID |
|---|---|
| Phishing | T1566 |
| Phishing via email attachment | T1566.001 |
| Phishing via spearphishing link | T1566.002 |

---

## 📚 Key Learnings

- Understood how TF-IDF captures meaningful patterns in text vs simple word counts
- Learned how stopword removal and stemming improve model accuracy
- Gained experience combining rule-based and ML approaches for better detection
- Practiced evaluating model performance using precision, recall, and F1-score

---

## 🔮 Future Improvements

- [ ] Upgrade to a transformer-based model (BERT / RoBERTa)
- [ ] Add URL analysis for embedded phishing links
- [ ] Build a simple web interface for real-time detection
- [ ] Train on a larger, more diverse dataset
- [ ] Add multilingual phishing detection

---

## 🛠️ Tools & Technologies

`Python` `NLTK` `Pandas` `scikit-learn` `TF-IDF` `Logistic Regression` `NLP`

---
MIT License

Copyright (c) 2026 Shyam Ravi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software to use, copy,modify, merge, publish, distribute, and/or sublicense for any purpose, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY DAMAGES ARISING FROM USE OF THIS SOFTWARE.

## ⚠️ Disclaimer

This project is built purely for **educational and research purposes** in a controlled home environment.

- All attack simulations were performed ONLY on systems I personally own and operate
- No unauthorized systems were accessed
- All findings are simulated in an isolated lab
- This tool is NOT intended for malicious use

The author takes NO responsibility for misuse of this project or any damage caused by applying these techniques outside of authorized environments.

# Code of Conduct

## Acceptable Use
This project may be used for:
- Educational and learning purposes
- Authorized security research
- Personal lab environments
- Academic projects

## Unacceptable Use
This project must NOT be used for:
- Unauthorized system access
- Malicious attack simulation
- Privacy violations
- Any illegal activities

## Reporting Issues
Report security concerns to: your@email.com

Violations of this code may result in
being banned from contributing.

## 👤 Author

**Shyam Ravi**
CEH | SOC Aspirant | Splunk SIEM
[LinkedIn](https://linkedin.com/in/) • [GitHub](https://github.com/)

---

> ⚠️ This project is built for educational and research purposes in cybersecurity threat detection.
