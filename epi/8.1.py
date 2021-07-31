R'''
Write a method that takes a sorted array and a key and returns the index of the first occurrence of
that key in the array.
'''

def first_occurence(a, l, u, key):
    R'''
    Mine. First I made it O(n) by finding key then naively scrolling down until finding another value.
    But now I am going to make sure a[0] is not key, then find key then `binary search` any other value less than key. This will be O(logn)
    '''
    if (not a) or (l > u):
        return None

    if a[0] == key:
        return 0

    while l <= u:
        m = l + (u - l) // 2
        if a[m] < key:
            l = m + 1
        elif a[m] > key:
            u = m - 1
        else:
            if a[l] == key:
                return l
            u = m
            while l <= u:
                m = l + (u - l) // 2
                if a[m] >= key:
                    u = m - 1
                elif a[m] < key:
                    l = m + 1
            return l

    return -1

def search_first_of_k(a, k):
    R'''
    Author's: His solution is beautiful and so simple.
    The fundamental idea of binary search is to maintain a set of candidate solutions. For the current problem, if we see the element at index i equals k, although we do not know whether i is the first element equal to k, we do know that no subsequent elements can be the first one. Therefore we remove all elements with index i + 1 or more from the candidates. Let’s apply the above logic to the given example, with k = 108. We start with all indices as candidates, i.e., with [0, 9]. The midpoint index, 4 contains k. Therefore we can now update the candidate set to [0, 3], and record 4 as an occurrence of k. The next midpoint is 1, and this index contains −10. We update the candidate set to [2, 3]. The value at the midpoint 2 is 2, so we update the candidate set to [3, 3]. Since the value at this midpoint is 108, we update the first seen occurrence of k to 3. Now the interval is [3, 2], which is empty, terminating the search—the result is 3.
    '''
    left, right, result = 0, len(a) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if k < a[mid]:
            right = mid - 1
        elif k == a[mid]:
            right = mid - 1 # Nothing to the right of mid can be solution
            result = mid
        else:
            left = mid + 1
    return result



a = [-14, -10 ,2, 108, 108, 243, 285, 285, 285, 401]
r = first_occurence(a, 0, len(a) - 1, 285)
print(r)
