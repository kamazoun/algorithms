r"""
TODO
"""
# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from node import Node

def sum_lists(head1: Node, head2: Node) -> Node:
    head_r = None
    result = None
    retenue = 0
    while (head1 is not None) or head2:
        a = b = 0
        if head1:
            a = head1.data
            head1 = head1.next
        if head2:
            b = head2.data
            head2 = head2.next
        r = a + b + retenue
        retenue = int(r / 10)
        if result:
            new_node = Node(r % 10)
            result.next = new_node
            result = result.next
        else:
            result = Node(r % 10)
            head_r = result
            
    return head_r


# ============= TESTS ================>

a = [1, 2, 3]
b = [4, 5,]

head_a = None
node = None
prev = None
for i in a:
    node = Node(i)
    if prev:
        prev.next = node
    else:
        head_a = node
    prev = node
head_b = None
node = None
prev = None
for i in b:
    node = Node(i)
    if prev:
        prev.next = node
    else:
        head_b = node
    prev = node


head_r = sum_lists(head_a, head_b)

head_r.traverse()
