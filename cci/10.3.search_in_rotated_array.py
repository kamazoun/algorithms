R'''
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.
EXAMPLE
Input:find 5 in {l5, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
'''

def search_r(arr, key):
    R'''
    Author's O(logn) for distinct elements
    '''
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if key == arr[mid]:
            return mid

        if arr[l] < arr[mid]: # left side is normally ordered
            if key >= arr[l] and key < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        elif arr[mid] < arr[l]: # right side is normally ordered
            if key > arr[mid] and key <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1
        elif arr[l] == arr[mid]:
            if arr[mid] != arr[r]:
                l = mid + 1
            else: # Search both halves
                for i in range(len(arr)):
                    if arr[i] == key:
                        return key


arr = [9, 9, 1, 2, 3, 5, 9]
mid = search_r(arr, 1)
print(mid)
