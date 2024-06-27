R'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

from node import Node

 
def partition(head: Node, x: int):
    R'''
    Mine: I had forgotten to return head.
    '''
    if not head:
        return head

    left = middle = right = None
    node = head

    while node:
        if node.data < x:
            if left:
                left.next = node
            else:
                head = node
            left = node
        else:
            if not middle:
                middle = node
            else:
                right.next = next
            right = node
    if left:
        left.next = middle
        return head
    else:
        return middle
 # Author's just uses two nodes head and tail and append before head and after tail


def partition_new(head: Node, x: int):
    if not head or not head.next:
        return head
    
    slow = head
    
    while slow.data < x:
        slow = slow.next

    fast = slow.next

    while fast:
        if fast.data < x:
            t = slow.data  # Yes, Python allows the swapping to be more beautiful
            slow.data = fast.data
            fast.data = t
            slow = slow.next
        fast = fast.next
    return head


node1 = Node(3)
node2 = Node(5)
node3 = Node(8)
node4 = Node(5)
node5 = Node(10)
node6 = Node(2)
node7 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

r = partition_new(node1, 5)

r.traverse()

# node1 = Node(1)
# node2 = Node(5)
# node3 = Node(2)
# node4 = Node(8)
# node5 = Node(3)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# r = partition_new(node1, 3)

# r.traverse()