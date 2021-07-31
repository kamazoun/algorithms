R'''
Design an algorithm that takes as input an array and a number, and determines if there are three
entries in the array (not necessarily distinct) which add up to the specified number. For example,
if the array is [11, 2, 5, 7, 3] then there are three entries in the array which add up to 21 (3, 7, 11 and
5, 5, 11). (Note that we can use 5 twice, since the problem statement said we can use the same entry
more than once.) However, no three entries add up to 22.
'''

def sum_2(a, n):
    R'''
    O(n)
    Assumes that a is sorted, as it is to be used with sum_3, else we'd sort it.
    '''
    i, j = 0, len(a) -1
    while i <= j:
        if (a[i] + a[j]) < n:
            i += 1
        elif (a[i] + a[j]) > n:
            j -= 1
        else:
            return True

    return False


def sum_3(a, n):
    R'''
    O(n^2)
    '''
    a.sort()
    return any(sum_2(a, n-i) for i in a) # This replaces everything below in the function

'''
    for i in a:
        v = n - a
        if sum_2(a, v):
            return True

    return False
'''

a = [11, 2, 5, 7, 3]
r = sum_3(a, int(input()))
print(r)
