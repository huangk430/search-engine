
# Python Search Engine - UCI ICS

This project is a search engine built from scratch 
that is capable of 10,000+ web pages, specifically UC 
Irvine's Information and Computer Sciences department, 
under harsh operational constriants. The average query 
response time is under 300ms.

## Installation

Use pip package manager to install BeautifulSoup, nltk

```bash
  pip install beautifulsoup4
  pip install --user -U nltk 
```
    
## Usage

In order to create your own search queries, 

Go to main.py and change line 183 from 
```javascript
directory = "/Users/kellyhuang/Downloads/DEV"
```

to 

```javascript
directory = "<mydirectory>"
```
This directory should hold the json files that you would like to create your search engine from.


Run main.py to create the partial indexes for each word.

Run sort.py to sort each partial index.

Run search.py to start your search queries - you will receive a list of urls that contain the query you are searching for, as well as the query response time.

## Demo


https://user-images.githubusercontent.com/64836972/147994290-c148a779-3712-49d9-844c-778b7dc096c1.mov



