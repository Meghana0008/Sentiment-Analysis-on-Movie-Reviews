# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import nltk
import re
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Download NLTK stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Load dataset from CSV
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df

# Text Preprocessing Function
def preprocess_text(text):
    text = str(text).lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
    words = text.split()  # Tokenization
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return " ".join(words)

# Load the dataset
df = load_dataset("movie_reviews.csv")

# Apply preprocessing
df['cleaned_review'] = df['Review'].apply(preprocess_text)

# Convert text to numerical representation using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)  # Limit vocabulary size
X = vectorizer.fit_transform(df['cleaned_review'])
y = df['Sentiment'].map({'Positive': 1, 'Negative': 0, 'Neutral': 2})  # Encode labels

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Function to Predict Sentiment for New Reviews
def predict_sentiment(review):
    cleaned_review = preprocess_text(review)
    transformed_review = vectorizer.transform([cleaned_review])
    prediction = model.predict(transformed_review)[0]
    sentiment_map = {1: "Positive", 0: "Negative", 2: "Neutral"}
    return sentiment_map[prediction]

sample_review = input("please enter a review")
print(f"Review Sentiment: {predict_sentiment(sample_review)}")
for i in range(10):
    sample_review = input("please enter a review")
    print(f"Review Sentiment: {predict_sentiment(sample_review)}")

