# Import libraries
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import nltk

# Download NLTK stopwords and tokenizer
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

# Load dataset
dataset_path = 'training.csv'  # Path to dataset file

data = pd.read_csv(dataset_path, encoding='latin-1', header=None)  # No headers in the CSV

data.columns = ["polarity", "id", "date", "query", "user", "text"]  # Assign column names

# Extract relevant columns
data = data[["polarity", "text"]]

# Preprocessing function
def preprocess_tweet(tweet):
    # Remove special characters, links, and numbers
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)
    tweet = re.sub(r'@\w+|#', '', tweet)  # Remove @mentions and hashtags
    tweet = re.sub(r'[^A-Za-z\s]', '', tweet)  # Remove non-alphabetic characters
    tweet = tweet.lower()  # Convert to lowercase
    tweet = word_tokenize(tweet)  # Tokenize
    # Remove stopwords
    tweet = [word for word in tweet if word not in stop_words]
    return " ".join(tweet)

# Apply preprocessing to all tweets
data['CleanedText'] = data['text'].apply(preprocess_tweet)

# Convert polarity into binary labels (0: negative, 1: positive)
data['polarity'] = data['polarity'].apply(lambda x: 1 if x == 4 else 0)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['CleanedText'])  # Feature matrix
y = data['polarity']  # Labels

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print results
print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)

