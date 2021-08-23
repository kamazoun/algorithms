R'''
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

def list_depths(root, l = [], level = 0):
    R'''
    Mine: brute force.
    O(n) or O(2^h)
    Looks like a modification of DFS.
    '''

    if root:
        if len(l) >= level:
            l[level].add(root)
            list_depths(root.left, l, level + 1)
            list_depths(root.right, l, level + 1)
        else:
            l.append(LinkedListSentinel)
            list_depth(root, l, level)

    return l

def list_depths(root):
    R'''
    Author's idea to use BFS. Same runtime.
    '''
    if not root:
        return []

    result = []
    current = LinkedListSentinel.add(root)

    while len(current) > 1: # because the sentinel takes 1 unit of length
        result.append(current) # a layer of depth added
        parents = current # will be used to extract direct children (at the same layer)
        current = LinkedListSentinel() # creates a new empty `level layer`
        node = parents.next
        while node:
            if node.left:
                current.add(node.left)
            if node.right:
                current.add(node.right)
            node = node.next

    return result
