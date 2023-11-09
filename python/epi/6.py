import math

def traversal_count(root) -> (int, int):
    l, r = 0, 0
    if root.left:
        l = traversal_count(root.left)
    if root.right:
        r = traversal_count(root.right)

    return (l+1, r+1)

def is_height_balanced(root):
    if not root:
        return True

    l, r = traversal_count(root)
    return abs(l-r) < 2

    #return is_height_balanced(root.left) and is_height_balanced(root.right)
