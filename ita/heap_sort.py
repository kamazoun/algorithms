R'''
#### We assume a max-heap. Some operations are exactly identical for min-heap.

## Left(i) = is the index of the left child of i (if it exists).
   For 0-based arrays indexing == 2 * i + 1
   For 1-based arrays indexing == 2 * i

## Right(i) = is the index of the right child of i (if it exists).
   For 0-based arrays indexing == 2 * i + 2
   For 1-based arrays indexing == 2 * i + 1

 ## Parent
   For 0-based arrays indexing == (i - 1) // 2
   For 1-based arrays indexing == i // 2
'''
def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

# Maintaining the heap property
def max_heapify(arr : list, i : int, heap_size = None):
    R'''
    We assume that the trees rooted at Left(i) and Right(i) are max-heaps, but arr[i] might be smaller than its children, thus violating the max-heap property. At each step, the largest of the elements arr[i], arr[Left(i)], and arr[Right(i)] is set as the root of the tree rooted at i. If arr[i] was the largest the procedure ends. Otherwise the largest is swapped with arr[i] and because the swap could have messed the heap property in the subtree rooted at the swapped index, we recursively call max_heapify() on the swapped index.
    '''
    if not heap_size:
        heap_size = len(arr) # Could be different than len(arr). For instance to prevent recursively calling beyond the necessary point
    l = left(i)
    r = right(i)
    largest = i # For now we assume that the heap property holds
    if (l < heap_size) and (arr[l] > arr[largest]):
        largest = l
    if (r < heap_size) and (arr[r] > arr[largest]):
        largest = r
    if largest != i: # The heap property at i wasn't observed
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest) # Because we might have messed the heap property for the subtree rooted at largest, due to the above swap


# Building a heap
def build_max_heap(arr):
    R'''
    Builds a max-heap out of arr.
    The elements [n // 2 ... n] are all leaves, so [0 ... n // 2 - 1] are roots.
    So we call max_heapify() on these in reversed order. What we obtain is a max-heap.
    '''
    heap_size = len(arr) # because we'll build the whole tree
    for i in reversed(range(heap_size // 2)):
        max_heapify(arr, i, heap_size)


def heapsort(arr):
    R'''
    We first make a max-heap out of arr, by calling build_max_heap().
    Then we swap max element with last element. We discard this last element by reducing heap_size.
    We call max_heapify to restore the heap property after the swap.
    We repeat this process until there is only two elements left.
    '''
    build_max_heap(arr)
    for i in reversed(range(1, len(arr))): # Until there is element 0 and 1 left
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0, i) # i == heap_size
