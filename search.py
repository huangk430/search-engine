from nltk.stem import PorterStemmer
import time
import numpy as np
from heapq import heapify, heappush, heappop

# support boolean logic!
'''
Once you have built the inverted index, you are ready to test document retrieval with queries. At the very least,
the search should be able to deal with boolean queries: AND only. If you wish, you can sort the retrieved documents
based on tf-idf scoring (you are not required to do so now, but it will be required for the final search engine).
This can be done using the cosine similarity method. Feel free to use a library to compute cosine similarity once you
have the term frequencies and inverse document frequencies (although it should be very easy for you to write your own
implementation). You may also add other weighting/scoring mechanisms to help refine the search results.
'''

porter = PorterStemmer()

sortedafile = open("sortedindex/a.txt", "r")
sortedbfile = open("sortedindex/b.txt", "r")
sortedcfile = open("sortedindex/c.txt", "r")
sorteddfile = open("sortedindex/d.txt", "r")
sortedefile = open("sortedindex/e.txt", "r")
sortedffile = open("sortedindex/f.txt", "r")
sortedgfile = open("sortedindex/g.txt", "r")
sortedhfile = open("sortedindex/h.txt", "r")
sortedifile = open("sortedindex/i.txt", "r")
sortedjfile = open("sortedindex/j.txt", "r")
sortedkfile = open("sortedindex/k.txt", "r")
sortedlfile = open("sortedindex/l.txt", "r")
sortedmfile = open("sortedindex/m.txt", "r")
sortednfile = open("sortedindex/n.txt", "r")
sortedofile = open("sortedindex/o.txt", "r")
sortedpfile = open("sortedindex/p.txt", "r")
sortedqfile = open("sortedindex/q.txt", "r")
sortedrfile = open("sortedindex/r.txt", "r")
sortedsfile = open("sortedindex/s.txt", "r")
sortedtfile = open("sortedindex/t.txt", "r")
sortedufile = open("sortedindex/u.txt", "r")
sortedvfile = open("sortedindex/v.txt", "r")
sortedwfile = open("sortedindex/w.txt", "r")
sortedxfile = open("sortedindex/x.txt", "r")
sortedyfile = open("sortedindex/y.txt", "r")
sortedzfile = open("sortedindex/z.txt", "r")

partialIndexMap = {
    'a': sortedafile,
    'b': sortedbfile,
    'c': sortedcfile,
    'd': sorteddfile,
    'e': sortedefile,
    'f': sortedffile,
    'g': sortedgfile,
    'h': sortedhfile,
    'i': sortedifile,
    'j': sortedjfile,
    'k': sortedkfile,
    'l': sortedlfile,
    'm': sortedmfile,
    'n': sortednfile,
    'o': sortedofile,
    'p': sortedpfile,
    'q': sortedqfile,
    'r': sortedrfile,
    's': sortedsfile,
    't': sortedtfile,
    'u': sortedufile,
    'v': sortedvfile,
    'w': sortedwfile,
    'x': sortedxfile,
    'y': sortedyfile,
    'z': sortedzfile,
}


def fileToURL(txtFile):
    urlMap = {}
    with open(txtFile) as f:
        line_list = [line.rstrip('\n') for line in f]
        for line in line_list:
            line = line.split(", ")
            urlMap[int(line[0])] = line[1]

    return urlMap


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

invertedIndex = dict()

def getPostingFromStart(partialIndexFile, word):
    '''
    Should have the pointer already!
    '''
    postings = []

    currLine = partialIndexFile.readline()
    while currLine:
        numlst = []
        numStr = ""
        processedLine = currLine.split(":")
        if processedLine[0] != word:
            return postings

        for char in processedLine[1]:
            if char.isnumeric():
                numStr += char
            else:
                if numStr != "":
                    numlst.append(int(numStr))
                    numStr = ""

        numlst = [numlst[i:i + 2] for i in range(0, len(numlst), 2)]
        numlst = [tuple(n) for n in numlst]  # list of tuples!

        postings.append(numlst[0])  # bc each one only has one item right now!
        currLine = partialIndexFile.readline()

    return postings

# get the posting
def getPosting(token, invertedIndexFile, pointerMap):
    if len(token) == 0:
        return []
    abrv = ""
    if len(token) < 2:
        abrv = token[0]
    else:
        abrv = token[0:2]

    bytesInAdvance = pointerMap[abrv]

    invertedIndexFile.seek(
        bytesInAdvance
    )  # go to the file where it has the start of the abbriveation!

    currLine = invertedIndexFile.readline()
    while currLine:
        processedLine = currLine.split(":")
        currentToken = processedLine[0]
        if token == currentToken:
            numlst = []
            numStr = ""
            processedLine = currLine.split(":")

            for char in processedLine[1]:
                if char.isnumeric():
                    numStr += char
                else:
                    if numStr != "":
                        numlst.append(int(numStr))
                        numStr = ""

            numlst = [numlst[i:i + 2] for i in range(0, len(numlst), 2)]
            numlst = [tuple(n) for n in numlst]  # list of tuples!

            return numlst

        elif currentToken > token:
            print("CUT OFF")
            return []
        currLine = invertedIndexFile.readline()

# given a list of postings, get the common ones between every single on the list
def getFinalPostingScore(queryWordPostingList):
    '''
    queryWordPostingList: a list of a lists of tuples!

    Postings (x:y) – document number and word count

    :return: A list with ONE list that has the COMBINED postings
    '''
    partialScoreMap = {}
    for postingList in queryWordPostingList:
        for posting in postingList:
            word = posting[0]
            freq = posting[1]
            if word in partialScoreMap:
                partialScoreMap[word] += freq
            else:
                partialScoreMap[word] = freq

    finalScorePosting = []
    for word, score in partialScoreMap.items():
        finalScorePosting.append((word, score))

    return finalScorePosting

def getDocID(singlePosting):
    return singlePosting[0]

def getTFIDFScore(tf, df, N):
    #w = (1+log(tf)) * log(N/df)
    return (1 + np.log(tf)) * np.log(N / df)


def startTimer():
    return time.time()

def printTimeElapsed(starTime):
    endTime = time.time()
    print("The seconds elapsed for this search is={0}".format(endTime -
                                                            startTime))



def readIndex(invertedIndexFile):
    '''
    Index the index!
    :return:
    '''
    pointerMap = {}
    currLine = invertedIndexFile.readline()
    currbytes = 0
    while currLine:
        processedLine = currLine.split(":")
        token = processedLine[0]
        abrv = ""
        bytes = len(currLine)
        if len(token) < 2:
            abrv = token[0]
        else:
            abrv = token[0:2]
        if abrv not in pointerMap:
            pointerMap[abrv] = currbytes
        currbytes += bytes

        currLine = invertedIndexFile.readline()
    return pointerMap
'''
READ THE MERGEDFILE.txt to build out the dictionary! 
'''

invertedIndexFile = open("mergedfile.txt", "r")

pointerMap = readIndex(invertedIndexFile)

urlMap = fileToURL("URLMap.txt")
searchQuery = ""
rankedUrls = []  # this list will just be of size 20! don't need to store mroe
stopTerm = "STOP"
N = len(urlMap)

# creating the min heap!
urlScores = []
heapify(urlScores)

while searchQuery != stopTerm:
    searchQuery = input("Enter your search query: ")
    startTime = startTimer()

    searchQueryWords = searchQuery.split()

    # tokenize and stem every word inside of searchArr!
    for i in range(len(searchQueryWords)):
        word = tokenize(searchQueryWords[i])
        word = stem(searchQueryWords[i])
        print("tokenized word=", word)
        searchQueryWords[i] = word

    if searchQuery != stopTerm:
        queryWordPostingList = [
        ]  # a list of all the postings from the individual search query terms
        for token in searchQueryWords:
            posting = getPosting(token, invertedIndexFile,
                                 pointerMap)  # will get a LIST of TUPLES
            # print("posting for", token, " ", posting)

            # SORT THE POSTING HERE so it's easier for merging!
            # posting.sort(key=lambda i: i[0])

            queryWordPostingList.append(
                posting)  # this will be a list with a list inside of tuples!

        finalPostingScore = getFinalPostingScore(queryWordPostingList)
        for posting in finalPostingScore:
            urlId = posting[0]
            tf = posting[1]
            df = len(finalPostingScore)
            tdidf = getTFIDFScore(tf, df, N)
            heappush(urlScores, (tdidf, urlId))
            if len(urlScores) > 20:
                heappop(urlScores)

        printTimeElapsed(
            startTime)  # dont need to account for the printing times!

        # these wont be sorted! will just be the top 20 url scores
        # TODO ACTUALLY SORT the urls!
        for tfidf, urlId in urlScores:
            print(urlMap[urlId])


# Letters!
sortedafile.close()
sortedbfile.close()
sortedcfile.close()
sorteddfile.close()
sortedefile.close()
sortedffile.close()
sortedgfile.close()
sortedhfile.close()
sortedifile.close()
sortedjfile.close()
sortedkfile.close()
sortedlfile.close()
sortedmfile.close()
sortednfile.close()
sortedofile.close()
sortedpfile.close()
sortedqfile.close()
sortedrfile.close()
sortedsfile.close()
sortedtfile.close()
sortedufile.close()
sortedvfile.close()
sortedwfile.close()
sortedxfile.close()
sortedyfile.close()
sortedzfile.close()

invertedIndexFile.close()
