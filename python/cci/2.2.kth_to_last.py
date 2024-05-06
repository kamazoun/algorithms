R'''
 Implement an algorithm to find the kth to last element of a singly linked list.
'''

class Node:
    def __init__(self):
        next = None

def kth_to_last_new(head: Node, k: int) -> Node:
    R"""
    The first idea I have here is to have a runner move k position before starting to move the head node.
    We need to pay attention of edge cases (such as when the list is less that k element long).
    """
    pass
def kth_to_last(head, k):
    R'''
    O(n) time and O(1) space.
    '''
    if not head:
        return None

    n = head
    while k > 0 and n:
        n = n.next
        k -= 1
    if not n.next:
        return n

    m = head
    while n.next:
        n = n.next
        m = m.next

    return m
