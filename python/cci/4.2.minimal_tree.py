R'''
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
'''

class BSTNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f'BST(data = ${self.data})\nleft = ${self.left}\nright = ${self.right}'

def minimal_tree(arr, s, n):
    R'''
    I'm starting to be recursive. O(2^log(n)) time and O(n) additional space.
    '''
    if s >= n - 1:
        return BSTNode(arr[s])
    m = (s + n - 1)  // 2 # For the example case, s + n - 1 yields better results than s + n
    top = BSTNode(arr[m], left = minimal_tree(arr, s, m), right = minimal_tree(arr, m+1, n))
    return top

arr = [1, 2, 3, 4, 5, 6, 7, 8]
a = minimal_tree(arr, 0, len(arr))
print(a)
