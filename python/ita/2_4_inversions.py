R'''
Let A[1 ... n] be an array of n distinct numbers. If i<j and A[i] > A[j] , then the pair (i, j) is called an inversion of A.

Give an algorithm that determines the number of inversions in any permutation
on n elements in O(n lg n) worst-case time. (Hint: Modify merge sort.)
'''



def count_inversions(arr, start, middle, end):
    inversions = 0

    a1 = arr[:middle + 1] + [float('inf')]
    a2 = arr[middle + 1:] + [float('inf')]

    i = j = 0
    k = start

    while k <= end:
        if a2[j] < a1[i]: # an inversion occured
            arr[k] = a2[j]
            inversions += (middle - k + 1)
            j += 1
            k += 1
        else:
            arr[k] = a1[i]
            i += 1
            k += 1

    return inversions


def merge_inversion_count(arr, start, end):
    # if arr is already sorted in ascending order, inversions == 0
    inversions = 0
    if start < end:
        middle = start + (end - start) // 2
        inversions += merge_inversion_count(arr, start, middle)
        inversions += merge_inversion_count(arr, middle + 1, end)
        inversions += count_inversions(arr, start, middle, end)

    return inversions


arr = [5, 4, 2, 3, 1]
r  = merge_inversion_count(arr, 0, len(arr) - 1)
print(r)
