R'''
A magic index in an array A[ 1 .•. n-1] is defined to be an index such that A[ i]
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
'''

def magic_index_no_dups(a):
    R'''
    O(logn)
    '''
    if not a:
        return -1

    l, r = 0, len(a) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if a[mid] < mid:
            l = mid + 1
        elif a[mid] == mid:
            return mid
        else:
            r = mid - 1
    return -1


def magic_index(a, l, r):
    #if not s, ...
    if l > r or (l < 0) or (r >= len(a)):
        return -1

    mid = l + (r - l) // 2

    if a[mid] < mid:
        # Should check if x == -1 then return, just to optimize
        x = magic_index(a, l, a[mid])
        y = magic_index(a, mid+1, r)
        return max(x, y)
    elif a[mid] == mid:
        return mid
    else:
        x = magic_index(a, l, mid-1)
        y = magic_index(a, a[mid], r)
        return max(x, y)


a = [-10, -5, -1, 1, 2, 3, 5, 7, 9, 12, 13  ]
r = magic_index(a, 0, len(a) - 1)
print(r)
