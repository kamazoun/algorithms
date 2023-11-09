
def binary_search(arr, key):
    R'''
    Normal binary search
    '''
    if not arr:
        return None

    l, u = 0, len(arr) - 1

    while l <= u:
        m = l + (u - l) // 2
        if arr[m] < key:
            u = m - 1
        elif arr[m] > key:
            l = m + 1
        else:
            return m

    return -1
