from typing import Tuple

from node import Node, build_linked_list



### The issue with this implementation is that it doesn't handle the case where the two linked lists have different lengths.
def follow_up(l1: Node, l2: Node) -> Node:
    def recurse(l1: Node, l2: Node) -> Tuple:
        if not l1 and not l2:
            return (None, 0)
        else:
            result = recurse(l1.next if l1 else None, l2.next if l2 else None)
            value = result[1]
            if l1:
                value += l1.data
            if l2:
                value += l2.data
            return (Node(value % 10, result[0]), 1 if value >= 10 else 0)
    result = recurse(l1, l2)
    if result[1]:
        return Node(1, result[0])
    return result[0]

# ============= TESTS ================>
a = [1, 2, 3]
b = [4, 5,]
C = [7, 1, 6]
d = [5, 9, 2]

head_a = build_linked_list(a)
head_b = build_linked_list(b)
head_r = follow_up(head_a, head_b)
head_r.traverse()
print("\n")
head_r = follow_up(build_linked_list(C), build_linked_list(d))
head_r.traverse()