r"""
TODO
"""
from node import Node

def sum_lists(head1: Node, head2: Node) -> Node:
    result = None
    retenue = 0
    while head1 or head2:
        if head1:
            a = head1.data
        if head2:
            b = head2.data
        r = a + b + retenue
        retenue = r / 10
        if result:
            result.next = Node(r % 10)
        else:
            result = Node(r % 10)
            
    return result

a = [1, 2, 3]
b = [4, 5, 6]

head_a = None
node = None
prev = None
for i in a:
    node = Node(i)
    if prev:
        prev.next = Node
    else:
        head_a = node
    prev = node

#print(head_a.data)
head_a = head_a.next
print(head_a.data)
for i in range(1):
    print(head_a.data)
    head_a = head_a.next