import InvertedIndexConstructor
from BooleanQueryEvaluator import booleanQueryEvaluator
from nltk.stem import PorterStemmer

invertedIndex = InvertedIndexConstructor.createInvertedIndex()

indexFile = open("Inverted_Index.txt", "w+")
resultFile = open("Results_File.txt", "w+")

stemmer = PorterStemmer()

for item in invertedIndex:
    indexFile.write(item)
    indexFile.write("\r\t" + str(invertedIndex[item].getFrequency()))
    indexFile.write("\r\t" + str(invertedIndex[item].getPostingList()) + "\r\r")

searchTerms = [('asus', 'google'), ('screen', 'bad'), ('great', 'tablet')]

for terms in searchTerms:
    resultList = booleanQueryEvaluator(terms[0], terms[1], invertedIndex)
    print(resultList)
    resultFile.write(terms[0] + ", " + terms[1])
    resultFile.write("\r\t" + str(resultList) + "\r\r")

