R'''
A heap is a tree-like data structure (in max-heap, max is root and any child key is smaller than its parent's. Vice-versa for min-heap), but the heap is not `completely` sorted. It can be compared to a binary tree (but not quite a binary search tree).
It is implemented as an array. In the array, the first index contains the root element. The next two indices of the array contain the root's children. The next four indices contain the four children of the root's two child nodes, and so on. Therefore, given a node at index i, its children are at indices 2i + 1 and 2i + 2, and its parent is at index floor((i-1)/2).
If the heap has N nodes and b branches for each node, its height (depth) is log(b)N. So for binary heap that gives log(2)N.
We can leverage that property to access the maximum element in the heap in O(logn) time. We perform this operation n times, each time extracting the max from the heap and into a sorted array. Thus, after n iterations we will have a sorted version of the input array.
'''

def swap(arr, a, b):
    R'''Done this way to keep in mind that python is by-value and not by-reference'''
    t_a = arr[a]
    t_b = arr[b]
    arr[a] = t_b
    arr[b] = t_a


def make_node_at_i(arr, i, l):
    l # length to consider for the tree
    node_i = i # the index of the node for this subtree (subtree at index i)
    left_i = 2*i+1 # left node index
    right_i = 2*i+2 # right node index
    if left_i < l and arr[left_i] > arr[node_i]:
        node_i = left_i
    if right_i < l and arr[right_i] > arr[node_i]:
        node_i = right_i

    if node_i != i: # if the max element is not the node
        # We put the max element as the node of this subtree
        swap(arr, node_i, i)

        # Now that we swapped the max with one of its children, we need to make sure to rearrange this child, so that it is the max of its own children
        make_node_at_i(arr, node_i, l) # with that we are sure that the child node is the max in its subtree (and recursively so)


# Will sort the arr using a max_heap_tree
def heap_sort_max(arr):
    for i in reversed(range(len(arr)//2)):
        make_node_at_i(arr, i, len(arr))
    # At this point we built the heap (max-heap tree in our case). It is 'just' a binary tree (not a bst though). The max's at the top, all the subtrees are 'ordered'
    # To sum up the most important, the max is at the beginning

    for curr_pos in reversed(range(len(arr))): # Why reversed? We start from the end to make sure that when we reach the beginning the first element (arr[0]) is the min 
        swap(arr, 0, curr_pos) # We put the max at the end

        make_node_at_i(arr, 0, curr_pos) # We remake a heap of the tree except the last len-curr_pos elements(the max, then the max and the second max, then ...)
        # At this point the heap (without the last len - curr_pos elements) is a max heap tree: the max is at beginning (and the previous max-es are at the end)
        # We will swap once more (to put the current max at curr_pos) and re-iterate.

    # arr is sorted
    return arr


print(heap_sort_max([-2, 5, 1, 0, 3, -4, -5, 7, 10, 8, 13, -14]))
