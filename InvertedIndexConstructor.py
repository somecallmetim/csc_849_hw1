class InvertedIndexTerm:
    def __init__(self, name, docId):
        self.__name = name
        self.__frequency = 1
        self.__postingList = []

        self.__postingList.append(docId)

    def addPosting(self, docId):
        if docId not in self.__postingList:
            self.__postingList.append(docId)

        self.__frequency += 1

    def getPostingList(self):
        return self.__postingList

    def getFrequency(self):
        return self.__frequency

    def getName(self):
        return self.__name

# from https://www.dotnetperls.com/punctuation-python
def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

from nltk.stem import PorterStemmer
import string

stemmer = PorterStemmer()

file = open("documents.txt", "r")

currentDocId = 0
currentlyInsideADocument = False

invertedIndex = {}

for line in file:
    for word in line.split():
        if "<" in word and "</" not in word:
            word = line.strip('<DOC ')
            word = word.split('>')
            currentDocId = word[0]
        elif ">" in word:
            pass
        else:
            key = str(word).lower()
            key = remove_punctuation(key)
            if key == "":
                break
            key = stemmer.stem(key)
            if key not in invertedIndex:
                invertedIndex[key] = InvertedIndexTerm(key, currentDocId)
            else:
                invertedIndex[key].addPosting(currentDocId)

for item in invertedIndex:
    print(item)
    print("\t" + str(invertedIndex[item].getFrequency()))
    print("\t" + str(invertedIndex[item].getPostingList()))