r"""
TODO
"""
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



def primary_case(h1: Node, h2: Node) -> Node:
    if not h1 or not h2:
        return h2 if not h1 else h1
    
    r = 0 # Retenue
    h3 = None
    head = None
    while h1 or h2:
        if h1 and h2:
            v = h1.data + h2.data + r
            d = v % 10
            r = v // 10
            n = Node(d)
            if h3:
                h3.next = n
                h3 = h3.next
            else:
                h3 = n
                head = h3
            h1 = h1.next
            h2 = h2.next
        else:
            if h1:
                h3.next = Node(h1.data)
                h1 = h1.next
            elif h2:
                h3.next = Node(h2.data)
                h2 = h2.next
            h3 = h3.next
    return head


def follow_up(h1: Node, h2: Node) -> Node:
    """The easiest way would be to traverse the list, save the encountered values in an array, perform the sum, reconstruct a list and return it.
    The time constraint would be the same but the space complexity would be O(n+m)
    """
    pass


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

print()

head_r = primary_case(head_a, head_b)

head_r.traverse()


print('FOLLOW UP CASE:\n\n\n')

print('123 + 45:')

head_r = follow_up(head_a, head_b)

head_r.traverse()

