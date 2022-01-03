import os
from nltk.stem import PorterStemmer
import json
from bs4 import BeautifulSoup
from posting import Posting
from collections import defaultdict

# variables we should keep track of
docID = 0
numUniqueTokens = 0
indexSize = 0
invertedIndex = defaultdict(list)

porter = PorterStemmer()

# make inverted index
# create a map with key of each word
'''
Steps
1: Traverse files and read all the JSON files
2: Open all the files and read it one at a time
3: Parsing (Read broken HTML)
4: Tokenization and Stemming
5. In Memory inverted index
6. Simple Index Serialization to disk


'''

def tokenize(word):
    result = ""
    letters = {
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    }
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

    for c in word:
        if c.lower() in letters or c in digits:
            result += c.lower()
    return result


def stem(word):
    # do stemming on the word!
    # https://www.datacamp.com/community/tutorials/stemming-lemmatization-python
    # just do porter.stem
    return porter.stem(word)

#takes in html and returns a list of tokens
def parseFile(raw_html):
    # specialChars = "©,.!:#$%^&*@()-_=+{}|\/?<>;'\""
    soup = BeautifulSoup(raw_html, "lxml")
    text = soup.get_text()
    # for specialChar in specialChars:
    #     text = text.replace(specialChar, " ")
    text = text.replace("\\t", " ")
    text = text.replace("\\r", " ")
    text = text.replace("\\n", " ")
    text = text.replace("\\", " ")
    return text.split()