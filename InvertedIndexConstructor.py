from nltk.stem import PorterStemmer
import string

# class to help track data for each term in our document list vocabulary
class InvertedIndexTerm:
    # constructor
    def __init__(self, name, docId):
        # fields
        self.__name = name
        self.__frequency = 1
        self.__postingList = []

        #start with the first docId the term is associated with in its postingList
        self.__postingList.append(docId)

    # add new occurance of term and increment frequency in which it appears
    def addPosting(self, docId):
        # only add the docId if it's not already in the postingList
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

def createInvertedIndex():
    stemmer = PorterStemmer()
    # this is the document (or hypothetical set of documents) we're scanning from
    file = open("documents.txt", "r")

    currentDocId = 0
    invertedIndex = {}

    # parse document line by line and add words to inverted index
    for line in file:
        # scane each line word for word
        for word in line.split():
            # individual documents in this toy example are delineated by tags ie <DOC 1> ~~~ </DOC 1>
                # this part of the if block detects document tags and sets the docId accordingly
            if "<" in word and "</" not in word:
                word = line.strip('<DOC ')
                word = word.split('>')
                currentDocId = word[0]
            elif ">" in word:
                pass
            # if the word/line isn't a document tag
            else:
                # makes the term all lower case
                key = str(word).lower()
                # attempts to remove all punctuation
                key = remove_punctuation(key)
                # if a word is all punctuation, ie ..., skips the word completely
                if key == "":
                    break
                # stems the now lower case and punctuation free word
                key = stemmer.stem(key)
                # if key isn't in the inverted index, it creates a new object and adds it to inverted index
                if key not in invertedIndex:
                    invertedIndex[key] = InvertedIndexTerm(key, currentDocId)
                # if key is in inverted index, program attempts to add new posting
                else:
                    invertedIndex[key].addPosting(currentDocId)

    return invertedIndex

