'''
Print all the subsets of a set
Link: https://www.youtube.com/watch?v=bGC2fNALbNU
'''
def allSubsets(given_set):
    subset = [None] * len(given_set)
    helper(given_set,subset,0)
def helper(given_set,subset,i):
    if i == len(given_set):
        print subset
    else:
        subset[i] = None
        helper(given_set,subset,i+1)
        subset[i] = given_set[i]
        helper(given_set,subset,i+1)

allSubsets([1,'abc'])