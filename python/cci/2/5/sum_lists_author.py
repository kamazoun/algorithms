r"""
TODO
"""
from node import Node
from node import build_linked_list

def sum_lists(l1: Node, l2: Node, carry = 0) -> Node:
    if not l1 and not l2 and not carry:
        return None
    else:
        value = carry
        if l1:
            value += l1.data
        if l2:
            value += l2.data
        result = Node(value % 10)
        if l1 or l2:
            more = sum_lists(l1.next if l1 else None, l2.next if l2 else None, 1 if value >= 10 else 0)
            result.next = more
        return result




# ============= TESTS ================>
a = [1, 2, 3]
b = [4, 5,]
C = [7, 1, 6]
d = [5, 9, 2]

head_a = build_linked_list(a)
head_b = build_linked_list(b)
head_r = sum_lists(head_a, head_b)
head_r.traverse()
print("\n")
head_r = sum_lists(build_linked_list(C), build_linked_list(d))
head_r.traverse()