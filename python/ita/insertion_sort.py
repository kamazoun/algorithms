


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr

# The only difference the asc is the change from > to <
def insertion_sort_desc(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] < key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

def insertion_sort_descending(arr):
    for j in reversed(range(len(arr)-1)):
        key = arr[j]
        i = j + 1
        while i < len(arr) and arr[i] > key:
            arr[i-1] = arr[i]
            i += 1
        arr[i-1] = key
    return arr



print(insertion_sort_desc([ 5, 6, 7, 1, -6, 8, 3]))
