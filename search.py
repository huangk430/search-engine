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