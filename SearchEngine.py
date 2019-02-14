import InvertedIndexConstructor
from BooleanQueryEvaluator import booleanQueryEvaluator
from nltk.stem import PorterStemmer

#create inverted index to use throughout program
invertedIndex = InvertedIndexConstructor.createInvertedIndex()

# set up file pointers to create/overwrite files for inverted index and search results
indexFile = open("Inverted_Index.txt", "w+")
resultFile = open("Results_File.txt", "w+")

# set up var for stemming
stemmer = PorterStemmer()

# write inverted index into file with easy to read format
for item in invertedIndex:
    indexFile.write(item)
    indexFile.write("\r\t" + str(invertedIndex[item].getFrequency()))
    indexFile.write("\r\t" + str(invertedIndex[item].getPostingList()) + "\r\r")

# set up search terms for this toy example
searchTerms = [('asus', 'google'), ('screen', 'bad'), ('great', 'tablet')]

# write search results into file with easy to read format
for terms in searchTerms:
    resultList = booleanQueryEvaluator(terms[0], terms[1], invertedIndex)
    resultFile.write(terms[0] + ", " + terms[1])
    resultFile.write("\r\t" + str(resultList) + "\r\r")

