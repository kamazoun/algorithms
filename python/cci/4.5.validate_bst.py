R'''
Implement a function to check if a binary tree is a binary search tree.
'''


def validate(root : BTNode, left = float('-inf'), right = float('inf')) -> bool:
    R'''
    Mine: O(n) + O(logn) (it's not O(2^h) space because we do not keep all the data till the end of the program. We first iterate through the left node, then when we're done --and delete the data from stack--, we iterate through the right node).
    A in-order traversal would not work for binary tree that are not full and complete (thus not bst) although their `bst property stands`.
    '''
    if not root:
        return True

    if not (left <= root.data <= right):
        return False

    return validate(root.left, left, root.data) and validate(root.right, root.data, right)
