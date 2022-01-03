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
# Letters!
afile = open("partialindex/a.txt", "w+")
bfile = open("partialindex/b.txt", "w+")
cfile = open("partialindex/c.txt", "w+")
dfile = open("partialindex/d.txt", "w+")
efile = open("partialindex/e.txt", "w+")
ffile = open("partialindex/f.txt", "w+")
gfile = open("partialindex/g.txt", "w+")
hfile = open("partialindex/h.txt", "w+")
ifile = open("partialindex/i.txt", "w+")
jfile = open("partialindex/j.txt", "w+")
kfile = open("partialindex/k.txt", "w+")
lfile = open("partialindex/l.txt", "w+")
mfile = open("partialindex/m.txt", "w+")
nfile = open("partialindex/n.txt", "w+")
ofile = open("partialindex/o.txt", "w+")
pfile = open("partialindex/p.txt", "w+")
qfile = open("partialindex/q.txt", "w+")
rfile = open("partialindex/r.txt", "w+")
sfile = open("partialindex/s.txt", "w+")
tfile = open("partialindex/t.txt", "w+")
ufile = open("partialindex/u.txt", "w+")
vfile = open("partialindex/v.txt", "w+")
wfile = open("partialindex/w.txt", "w+")
xfile = open("partialindex/x.txt", "w+")
yfile = open("partialindex/y.txt", "w+")
zfile = open("partialindex/z.txt", "w+")

# Numbers
numberfile = open("partialindex/numbers.txt", "w+")

partialIndexFileList = [
    afile, bfile, cfile, dfile, efile, ffile, gfile, hfile, ifile, jfile,
    kfile, lfile, mfile, nfile, ofile, pfile, qfile, rfile, sfile, tfile,
    ufile, vfile, wfile, xfile, yfile, zfile, numberfile
]

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

# gets frequency of word in a doc
def getFrequencyMap(wordList):
    freqMap = defaultdict(int)
    for word in wordList:
        freqMap[word] += 1
    return freqMap
    
def getPartialIndexFile(word):
    '''
    Return the file that it should write to
    '''
    firstChar = word[0].lower()
    if firstChar == 'a':
        return afile
    if firstChar == 'b':
        return bfile
    if firstChar == 'c':
        return cfile
    if firstChar == 'd':
        return dfile
    if firstChar == 'e':
        return efile
    if firstChar == 'f':
        return ffile
    if firstChar == 'g':
        return gfile
    if firstChar == 'h':
        return hfile
    if firstChar == 'i':
        return ifile
    if firstChar == 'j':
        return jfile
    if firstChar == 'k':
        return kfile
    if firstChar == 'l':
        return lfile
    if firstChar == 'm':
        return mfile
    if firstChar == 'n':
        return nfile
    if firstChar == 'o':
        return ofile
    if firstChar == 'p':
        return pfile
    if firstChar == 'q':
        return qfile
    if firstChar == 'r':
        return rfile
    if firstChar == 's':
        return sfile
    if firstChar == 't':
        return tfile
    if firstChar == 'u':
        return ufile
    if firstChar == 'v':
        return vfile
    if firstChar == 'w':
        return wfile
    if firstChar == 'x':
        return xfile
    if firstChar == 'y':
        return yfile
    if firstChar == 'z':
        return zfile
    else:
        return numberfile


print(f'Number of indexed documents: {numIndexDocuments}')
print(f'Number of unique tokens: {numUniqueTokens}')
print(f'Total Size of Index: {indexSize}')

# probably call a function to build it!
#
# with open("fileindex.txt", "w") as f:
#     for k, v in invertedIndex.items():
#         valueString = ""
#         for tup in v:
#             valueString += f"({tup[0]}, {tup[1]}) "
#         f.write(f"{k}: {valueString}\n")
#

# loop over all the different file pointers!

# Letters!
afile.close()
bfile.close()
cfile.close()
dfile.close()
efile.close()
ffile.close()
gfile.close()
hfile.close()
ifile.close()
jfile.close()
kfile.close()
lfile.close()
mfile.close()
nfile.close()
ofile.close()
pfile.close()
qfile.close()
rfile.close()
sfile.close()
tfile.close()
ufile.close()
vfile.close()
wfile.close()
xfile.close()
yfile.close()
zfile.close()

# Numbers!
numberfile.close()