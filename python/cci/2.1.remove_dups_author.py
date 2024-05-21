r"""
Because the cci/2.1.remove_dups.py file is large enough due to the new additions I brought to it, I decided to put the author implementation in a different file.
Why was it necessary to add the author implementation, although it has the same time and space complexities as mine?
Because the implementation of the author is leaner and more beautiful. For instance:
- In the simple case, it implemented successfully one technique that I tried and found difficult to `prettify`, namely, it would `jump` consecutive nodes that were already in the hash table.
  This means that if it encounters this list: 1 -> 2 -> 2 -> 3 -> 1 -> 1 -> 1, it would remove the 3 1s at the end in one go.
  Also, the author nicely used a set instead of a dict.
- In the efficient case, the implementation of the author did not make use of the `is_seen` flag that I used, also it did not use a `prev` node.

All the implementations of the author are for a singly linked list.
"""

from node import Node
def simple(node: Node):
    hash_table = set()  # Note: a simple set works well here
    prev = None
    while node:
        if node.data in hash_table:
            prev.next = node.next  # Note: this works because at the start, the hash table is empty
        else:
            hash_table.add(node.data)
            prev = node  # Note: It is actually this assignment (because it is only here) that allows the algorithm to `jump` consecutive nodes that were already seen
        node = node.next

def efficient(head: Node):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                pass

# TODO: I stopped there to think of a small issue: why is node set to node.next in line 23. Why not prev.next?
# The same goes for current that would have been set to current.next instead of runner.next?