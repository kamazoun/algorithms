R'''
A natural implementation for a search engine is to retrieve documents that match the set of words in
a query by maintaining an inverted index. Each page is assigned an integer identifier, its documentID. An inverted index is a mapping that takes a word `w` and returns a sorted array of page-ids which contain `w`—the sort order could be, for example, the page rank in descending order. When a query contains multiple words, the search engine finds the sorted array for each word and then computes the intersection of these arrays—these are the pages containing all the words in the query. The most computationally intensive step of doing this is finding the intersection of the sorted arrays.

Write a program which takes as input two sorted arrays, and returns a new array containing elements that are present in both of the input arrays. The input arrays may have duplicate entries, but the returned array should be free of duplicates. For example, the input is [2, 3, 3, 5, 5, 6, 7, 7, 8, 12] and [5, 5, 6, 8, 8, 9, 10, 10], your output should be [5, 6, 8].
'''
import collections

def intersection(a, b):
    R'''
    Mine: O(a + b) but with O(max(a, b)) space.
    Author's is O(a + b) and O(1) space
    If one set is much smaller than the other we can iterate through it, and binary search in the second. This would give O(smal*log(large)). This is the best solution when there is a huge difference in size between the two sets.
    '''
    ht = collections.defaultdict(int)
    for i in a:
        ht[i] += 1

    for i in b:
        if ht[i] != 0:
            ht[i] = -1

    c = [k for (k, v) in ht.items() if v == -1]
    return c


def inter_auth(a, b):
    R'''
    Author's O(a + b) and O(1) space.
    If one set is much smaller than the other we can iterate through it, and binary search in the second. This would give O(smal*log(large)). This is the best solution when there is a huge difference in size between the two sets.
    '''
    ia = ib = 0
    c = []
    while(ia < len(a)) and (ib < len(b)):
        if a[ia] < b[ib]:
            ia += 1
        elif a[ia] == b[ib]:
            if len(c) <= 0 or c[-1] != a[ia]: c.append(a[ia])
            ia += 1
            ib += 1
        else:
            ib += 1
    return c

a = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
b = [5, 5, 6, 8, 8, 9, 10, 10]
c = inter_auth(a, b)
print(c)
