import pandas as pd
import re
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dataset_path = 'training.csv'
test_dataset_path = 'test.csv'
stop_words_path = 'stop-words-list.txt'

data = pd.read_csv(dataset_path, encoding='latin-1', header=None)
test_data = pd.read_csv(test_dataset_path, encoding='latin-1', header=None)
stop_words_file = open(stop_words_path, "r")

stop_words = set(stop_words_file.read().split("\n"))

stop_words_file.close()

data.columns = ["polarity", "id", "date", "query", "user", "text"]
test_data.columns = [
    "textID", "text", "sentiment", "time", "user_age", "country",
    "population", "land_area", "density"
]

data = data[["polarity", "text"]]
test_data = test_data[["text", "sentiment"]]


def preprocess_tweet(tweet):
    tweet = re.sub(r'[^A-Za-z\s]', '', tweet)
    tweet = tweet.lower()
    tweet = word_tokenize(tweet)
    tweet = [word for word in tweet if word not in stop_words]
    return " ".join(tweet)


data['CleanedText'] = data['text'].apply(preprocess_tweet)

test_data['CleanedText'] = test_data['text'].fillna("").astype(str).apply(preprocess_tweet)

data['polarity'] = data['polarity'].apply(lambda x: 1 if x == 4 else 0)

test_data['polarity'] = test_data['sentiment'].fillna("").astype(str).apply(
    lambda s: {"negative": 0, "positive": 1, "neutral": 0}.get(s.lower(), 0))

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['CleanedText'])
y = data['polarity']

X_eval = vectorizer.transform(test_data['CleanedText'])
y_eval = test_data['polarity']

model = LogisticRegression()
model.fit(X, y)

y_eval_pred = model.predict(X_eval)

accuracy = accuracy_score(y_eval, y_eval_pred)

print(f"Accuracy: {accuracy}")
