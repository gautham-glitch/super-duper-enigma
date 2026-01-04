####################prep###########################################
import re, os, warnings, pandas as pd
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Silence warnings
warnings.filterwarnings("ignore")
from datetime import datetime
start = datetime.now()

# Download NLTK assets once
import nltk
for asset in ['punkt', 'wordnet', 'stopwords']:
    nltk.download(asset, quiet=True)

stop_words = set(stopwords.words('english'))

def preprocess_headlines(headlines: list[str]) -> list[str]:
    """
    Cleans and tokenizes headlines using TextBlob.
    Removes URLs, digits, stopwords, and lemmatizes tokens.
    """
    return [
        " ".join([
            word.lemmatize() for word in TextBlob(
                re.sub(r"\d+|http\S+|www\S+|https\S+", "", text.lower())
            ).words
            if word.isalpha() and word.lower() not in stop_words
        ])
        for text in headlines
    ]

####################load###########################################
import kagglehub
path = kagglehub.dataset_download("poushal02/fake-news-detector-full-dataset")
csv_path = os.path.join(path, "Fake News Detector.csv")
df = pd.read_csv(csv_path)

df["combined"] = df["title"].fillna("") + " " + df["text"].fillna("")
df = df.drop_duplicates(subset="combined").reset_index(drop=True)

headlines = df["combined"].tolist()
labels = df["label"].tolist()

####################train###########################################
cleaned = preprocess_headlines(headlines)

X_train, X_test, y_train, y_test = train_test_split(cleaned, labels, test_size=0.2, random_state=42)

# Define pipeline
pipeline = Pipeline([
    ('vectorizer', HashingVectorizer(
        n_features=2**16,
        stop_words='english',
        ngram_range=(1, 1),
        alternate_sign=False
    )),
    ('classifier', PassiveAggressiveClassifier(
        max_iter=100,
        tol=1e-2,
        random_state=42
    ))
])

pipeline.fit(X_train, y_train)

print(f"✅ Accuracy on test set: {pipeline.score(X_test, y_test):.2f}")
print(f"✅ Cross-val accuracy: {cross_val_score(pipeline, X_train, y_train, cv=5).mean():.2f}")
print(classification_report(y_test, pipeline.predict(X_test)))

joblib.dump(pipeline, "news_pipeline.pkl")

####################real world test###########################################
from collector import article_find
def predict_article(url: str) -> tuple[str, float, any]:
    raw_text = article_find(url)
    cleaned = preprocess_headlines([raw_text])
    vect = pipeline.named_steps['vectorizer'].transform(cleaned)
    
    pred = pipeline.named_steps['classifier'].predict(vect)[0]
    label_map = {0: "Fake News", 1: "Real News"}

    if hasattr(pipeline.named_steps['classifier'], "predict_proba"):
        prob = pipeline.named_steps['classifier'].predict_proba(vect)[0]
        confidence = round(max(prob) * 100, 2)
    else:
        score = pipeline.named_steps['classifier'].decision_function(vect)[0]
        confidence = round(abs(score) * 10, 2)

    return label_map[pred], confidence, vect

site = "https://www.toronto99.com/2025/04/04/the-purge-conservatives-fire-5th-candidate/"
label, confidence, text_vect = predict_article(site)
print(f"🧠 Prediction: {label} ({confidence}% confidence)")
print(datetime.now() - start)

