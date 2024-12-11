import csv
from nltk.tokenize import word_tokenize, sent_tokenize

read_file = open('somefile.txt', 'r')
lines = read_file.readlines()

n = len(lines)

rows = [["NewsBody", "NewsHeadline", "label", "WordTokensLength", 'SentTokensLength']]

for i in range(0,n,3):
    row = [lines[i], lines[i + 1], lines[i + 2], len(word_tokenize(lines[i])), len(sent_tokenize(lines[i]))]
    rows.append(row)

with open("output.tsv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    csvwriter.writerows(rows)