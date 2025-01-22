import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("training.csv", encoding='latin1')
sentences = df.iloc[:, 5].tolist()

labels = df.iloc[:, 0].tolist()

stop_words_file = open("stop-words-list.txt", "r")
stop_words = stop_words_file.read().split("\n")
stop_words_file.close()

for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r'[^a-zA-Z\s]', '', sentences[i])
    tokens = nltk.word_tokenize(sentences[i])
    filtered_tokens = [token for token in tokens if token not in stop_words]
    sentences[i] = filtered_tokens
    sentences[i] = " ".join(sentences[i])

for i in range(len(sentences[:5])):
    print(sentences[i])

tfidf = TfidfVectorizer()

result = tfidf.fit_transform(sentences)

decision_tree = DecisionTreeClassifier()
decision_tree.fit(result, labels)
# print(decision_tree.predict(["she has to quit her company, such a shame"]))
print(decision_tree.predict(result))
