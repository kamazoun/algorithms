'''
Counting sort works by calculating (counting) the frequency of an int in the array to sort, then from the min value puts the int in the array according to itsd frequency (the number of times it occurs).
These implementation work only with int (no char, no float, no custom types...)
The implementation with dict works with negative values. The implementation with list doesn't.
A way to make them work with char, would be to convert the char to its ASCII value.
Their time complexities average O(n + const) where const depends mainly on the range of the values in the array to sort (max - min, min with list == 0) and the most frequent term.
'''

def counting_sort_list(arr):
    r'''
arr is the array to sort
Returns the sorted array
The first problem with this implementation is that it allocates a lot of potentially useless memory: for instance to sort 99, 500, 999, we will allocate and array count of 999 elements. To try to solve this, I will instead use a dict for count variable.
The second problem is that we need to know the max number in the array to sort (assuming sorting numbers in increasing fashion), else we need to use the biggest num (int, float, or whatever we are sorting) on the underlying system.
The third problem is that it doesn't sort neither negative numbers nor floats
But it is still an O(n + k*max) with n the length of the array to sort, k the frequency of the most common term and max the largest int in the array.
'''
    if len(arr) < 2:
        return arr
    
    max = arr[0]

    for i in arr:
        if i > max: max = i

    count = [0]*(max+1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    z = 0
    for i in range(max + 1):
        while count[i] > 0: # frequency (number of times) an int appears in arr
            arr[z] = i
            z += 1
            count[i] -= 1
            
    return arr



def counting_sort_dict(arr):
    r'''
arr is the array to sort
Returns the sorted array
The goal of this implementation is to solve the three flaws of the original counting_sort
But it can only sort ints (positive and negative). No chars nor floats.
It is now an O(n + (k+1)*(max-min)) with n the length of the array to sort, k the frequency of the most common term and max and min the largest and smallest ints in the array.
'''
    if len(arr) < 2:
        return arr
    
    max = arr[0]
    min = arr[0]
    count = {}

    for i in arr:
        if i > max: max = i
        if i < min: min = i

    for i in range(min, max + 1):
        count[i] = 0 # the method requiring to check count.key() would take O(nlogn), so instead we do that

    for i in arr:
        count[i] += 1

        
    z = 0
    for i in range(min, max + 1):
        while count[i] > 0: # frequency (number of times) an int appears in arr
            arr[z] = i
            z += 1
            count[i] -= 1
            
    return arr


print(counting_sort_dict([-2, 5, 1, 0, 3, -6, -2, -2]))
