

def merge(arr, start, middle, end):
    R'''
    The array contains two sorted arrays [start to middle] and [middle + 1 to end]
    Sorts the elements of the array from start to end.
    start and end refer to index in the array not the indexes 0 and len(arr)-1
    '''

    l1 = middle - start + 1
    l2  = end - middle

    # To prevent resizing the array to append the infinity sentinel
    a1 = []*(l1 + 1)
    a2 = []*(l2 + 1)

    a1 = arr[start : middle+1]
    a1.append(float('inf'))
    a2 = arr[middle+1 : end+1] # Do not forget to include end: end + 1
    a2.append(float('inf'))

    i = j = 0
    print(a1, a2, i, j)
    k = start
    while k <= end:
        if a1[i] < a2[j]:
            arr[k] = a1[i]
            k += 1
            i += 1
        else:
            arr[k] = a2[j]
            k += 1
            j += 1


def merge_sort(arr, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(arr, start, middle)
        merge_sort(arr, middle+1, end)
        merge(arr, start, middle, end)
        print(arr)

    return arr

a = merge_sort([5, 4, 9, 5, 6, -6, 8], 0, 6)
print(a)
