# Model Notes

## Algorithm
Logistic Regression (scikit-learn)

## Feature Extraction
TF-IDF Vectorizer
- Max features: 5000
- N-gram range: (1, 2) — unigrams and bigrams

## Dataset
SMS Spam Collection Dataset (UCI ML Repository)
- ~5,500 labeled messages
- Labels: ham (legitimate) / spam (phishing)

## Observations
- TF-IDF with bigrams performed better than unigrams alone
- Rule-based keyword filter catches obvious phishing phrases before the ML model
- Logistic Regression is lightweight and fast for this text classification task

## Future Improvements
- Try BERT or DistilBERT for better contextual understanding
- Add URL feature extraction
- Train on email datasets (not just SMS)