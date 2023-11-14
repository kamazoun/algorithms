'''
O(n^2)
Actually I find this algorithm hard to wrap your head around, because it starts form the begining, 'swaps' each value in the while loop if they are bigger than the current key...
'''

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key: # from key at position i, will move `up` one notch all the arr[i] > key, 0 <= i < k, and insert key at the position of the last arr[i] > key (which by now would be at i+1)  
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

    return arr

print(insertion_sort([-2, 5, 1, 0, 3, -6, -2, -2]))
