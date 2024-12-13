import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

read_file = open('somefile.txt', 'r')
lines = read_file.readlines()

n = len(lines)

rows = [["NewsBody", "NewsHeadline", "label", "WordTokensLength", 'SentTokensLength', 'TokensFrequency']]

for i in range(0,n,3):
    tokens = word_tokenize(lines[i])
    tokens_freq = nltk.FreqDist(tokens)
    row = [lines[i], lines[i + 1], lines[i + 2], len(tokens), len(sent_tokenize(lines[i])), tokens_freq.items()]
    rows.append(row)

with open("output.tsv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    csvwriter.writerows(rows)