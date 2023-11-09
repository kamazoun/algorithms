

def odd_even(arr):
    R'''
    Your input is an array of
integers, and you have to reorder its entries so that the even entries appear first. This is easy if you
use O(n) space, where n is the length of the array. However, you are required to solve it without
allocating additional storage.

    Although we have embedded loops, we still run at O(n) time, as we only read elements of the arrays once.
    '''
    even = 0
    odd = len(arr) - 1

    while even < odd:
        while even < odd and arr[even] % 2 == 0:
            even += 1

        while even < odd and arr[odd] % 2 == 1:
            odd -= 1

        if even < odd:
            arr[odd], arr[even] = arr[even], arr[odd]
            even += 1
            odd -= 1

    return arr

print(odd_even([1, 2, 5, 7, 8]))
