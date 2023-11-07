R'''
Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
'''

def is_balanced(root):
    R'''
     Mine: O(n) time and O(h) space, h: height of the tree
    '''
    if not root:
        return (True, -1)

    x, l = is_balanced(root.left)
    if not x:
        return (False, -1)
    y, r = is_balanced(root.right)

    return (y and abs(l - r) <= 1, max(l, r) + 1)
