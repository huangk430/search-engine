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

# invertedIndex = fileToIndex("fileindex.txt")
urlMap = fileToURL("URLMap.txt")
# print(urlMap)
searchQuery = ""
rankedUrls = []  # this list will just be of size 20! don't need to store mroe
stopTerm = "STOP"
N = len(urlMap)

# creating the min heap!
urlScores = []
heapify(urlScores)



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
