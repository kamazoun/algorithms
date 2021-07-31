# Three methods are presented here:
## The `obvious` one: We check that each tree root is larger than or equal to the max of its left subtree and smaller than or equal to the min of its right subtree
## The `author's` one: We pass down and tighten constraints down the tree. At the beginning each node can have values between -inf and inf.
## The `clever` one: an in-order traversal of a bst should lay an ordered array: Can be implemented with DFS or BFS


R'''
Write a program that takes as input a binary tree and checks if the tree satisfies the BST property.
'''


def is_bst(tree):
    R'''
    O(n) time and O(h) space, h being the height of the tree
    '''
    if not tree:
        return (True, float('inf'), float('-inf'))
    if not (tree.left.data <= tree.data <= tree.right.data):
        return (False, 0, 0) # From the moment it's False the values won't be checked

    l_state, l_min, l_max = is_bst(tree.left)
    if not l_state or l_min > l_max:
        return (False, 0, 0) # From the moment it's False the values won't be checked

    r_state, r_min, r_max = is_bst(tree.right)
    if not r_state or r_min > r_max:
        return (False, 0, 0) # From the moment it's False the values won't be checked

    return ((l_max <= tree.data <= r_min), l_min, r_max)


def is_bst(tree, left = float('-inf'), right = float('inf')):
    R'''
    This method is based of author's. O(n) time and O(h) space.
    The underlying idea is to pass constraints down the tree.
    The left subtree values can go from the lower limit until the parent node value.
    And the right subtree values go from the parent node value to the upper limit
    '''
    if not tree:
        return True

    return (left <= tree.data <= right) and is_bst(tree.left, left, tree.data) and is_bst(tree.right, tree.data, right)


def is_bst(tree):
    R'''
    O(n) time and space.
    An in-order traversal should lead to an ascending sorted array.
    Here we optimize by doing a BFS search instead of a DFS, so that if the BST condition is broken at a certain level, we won't go any deeper to find it.
    '''
    def check_bst(tree, l, r):
        if not (l <= tree.data  <= r):
            return False
        tree.visited = True

    q = Collections.deque()
    q.append((tree, float('-inf'), float('inf')))

    while q:
        n, l, r = q.popleft()
        if (not n) or (n.visited): continue
        if not check_bst(n, l, r):
            return False

        q.append(n.left, l, n.data)
        q.append(n.rigth, n.data, r)

    return True



def is_bst(tree, arr = []):
        R'''
        O(n) time and space.
        An in-order traversal should lead to an ascending sorted array. DFS
        '''
    if tree.left:
        x = is_bst(tree.left)
        if not x: return False
    if not (tree.data >= arr[-1]):
        return False
    arr.append(tree.data)
    if tree.rigth:
        x = is_bst(tree.right)
        if not x: return False
