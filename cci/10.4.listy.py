R'''
You are given an array like data structure Listy which lacks a size method. It does, however, have an elementAt ( i) method that returns the element at index i in 0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data structure only supports positive integers.) Given a Li sty which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.
'''


def search_listy(x : int, l : Listy, i : int):
    R'''
    Mine: O(logn).
    Author's solution first finds the `end` of array, then perform binary search on it.
    '''
    if not i:
        i = x

    if (l.element_at(i) == -1) or l.element_at(i) > x:
        return search_listy(x, l, i - (i // 2))

    elif l.element_at(i) == x:
        return i

    else:
        return search_listy(x, l, i + (i // 2))
