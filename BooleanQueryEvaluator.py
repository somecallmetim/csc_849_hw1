from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def findIntersection(queryOnePostingList, queryTwoPostingList):
    resultList = []

    qOneIterator = 0
    qTwoIterator = 0
    qOneSize = len(queryOnePostingList)
    qTwoSize = len(queryTwoPostingList)

    # print(resultList) # print statement

    while(True):
        if qOneIterator >= qOneSize or qTwoIterator >= qTwoSize:
            break

        if int(queryOnePostingList[qOneIterator]) == int(queryTwoPostingList[qTwoIterator]):

            # print(str(qOneIterator) + ' [' + str(queryOnePostingList[qOneIterator]) + "], "
            #       + str(qTwoIterator) + ' [' + str(queryTwoPostingList[qTwoIterator]) + ']') # print statement

            resultList.append(queryOnePostingList[qOneIterator])
            # print(resultList) # print statement
            qOneIterator += 1
            qTwoIterator += 1
        elif int(queryOnePostingList[qOneIterator]) < int(queryTwoPostingList[qTwoIterator]):
            qOneIterator += 1
        else:
            qTwoIterator += 1
    # print("===========================================================================")
    # print("===========================================================================")
    return resultList

def getQueryPostingList(query, invertedIndex):
    return invertedIndex[stemmer.stem(query)].getPostingList()

def booleanQueryEvaluator(queryOne, queryTwo, invertedIndex):
    queryOnePostingList = getQueryPostingList(queryOne, invertedIndex)
    queryTwoPostingList = getQueryPostingList(queryTwo, invertedIndex)

    # print("===========================================================================")
    # print("===========================================================================")
    # print(queryOne + ", " + queryTwo)

    return findIntersection(queryOnePostingList, queryTwoPostingList)