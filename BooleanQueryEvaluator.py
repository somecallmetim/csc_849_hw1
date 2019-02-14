from nltk.stem import PorterStemmer

# set up var for stemming
stemmer = PorterStemmer()

# this function finds the intersection of two ordered sets represented by python lists
def findIntersection(queryOnePostingList, queryTwoPostingList):

    # where common items between the two lists are recorded
    resultList = []
    # iterators for each list
    qOneIterator = 0
    qTwoIterator = 0
    # overall size of each list is recorded to prevent boundary errors
    qOneSize = len(queryOnePostingList)
    qTwoSize = len(queryTwoPostingList)

    # run until internal condition met
    while(True):
        # break once either of the iterators reaches respective list boundary
        if qOneIterator >= qOneSize or qTwoIterator >= qTwoSize:
            break

        # this is run when we find a match. the list items appear as strings, so must be typecast
        if int(queryOnePostingList[qOneIterator]) == int(queryTwoPostingList[qTwoIterator]):
            # add document id to resultList
            resultList.append(queryOnePostingList[qOneIterator])

            # increment both iterators
            qOneIterator += 1
            qTwoIterator += 1

        # increment the iterator that points to the smaller value
        elif int(queryOnePostingList[qOneIterator]) < int(queryTwoPostingList[qTwoIterator]):
            qOneIterator += 1
        else:
            qTwoIterator += 1

    return resultList

# this gets the postingList for the query term
def getQueryPostingList(query, invertedIndex):
    return invertedIndex[stemmer.stem(query.lower())].getPostingList()

# this method runs everything else in the module
def booleanQueryEvaluator(queryOne, queryTwo, invertedIndex):
    # get posting lists
    queryOnePostingList = getQueryPostingList(queryOne, invertedIndex)
    queryTwoPostingList = getQueryPostingList(queryTwo, invertedIndex)

    # find and return postList intersections
    return findIntersection(queryOnePostingList, queryTwoPostingList)

