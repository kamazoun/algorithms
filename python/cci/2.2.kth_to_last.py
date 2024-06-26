R'''
 Implement an algorithm to find the kth to last element of a singly linked list.
'''

from node import Node


def kth_to_last_recursive(head: Node, k):
    if not head.next:
        return 1, head
    else:
        r, n = kth_to_last_recursive(head.next, k)
        if r == k:
            return r, n
        else:
            return r + 1, head

def kth_to_last_new(head: Node, k: int) -> Node:
    R"""
    The first idea I have here is to have a runner move k position before starting to move the head node.
    We need to pay attention of edge cases (such as when the list is less that k element long).
    """
    runner = head
    i = 0
    while runner and i < k:
        runner = runner.next
        i += 1

    current = head
    while runner:
        current = current.next
        runner = runner.next
    return current


head = Node(0)
node = head
for i in range(1, 10):
    node.next = Node(i)
    node = node.next

r, node = kth_to_last_recursive(head, 11)
print(node)




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

