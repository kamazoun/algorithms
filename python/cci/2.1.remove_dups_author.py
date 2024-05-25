r"""
Because the cci/2.1.remove_dups.py file is large enough due to the new additions I brought to it, I decided to put the author implementation in a different file.
Why was it necessary to add the author implementation, although it has the same time and space complexities as mine?
Because the implementation of the author is leaner and more beautiful. For instance:
- In the simple case, the author nicely used a set instead of a dict.
- In the efficient case, the implementation of the author did not make use of the `is_seen` flag that I used, also it did not use a `prev` node. Moreover, by including the famous `else`, that I missed, the author made this simple looking algorithm work, quite efficiently, because it could `jump` and remove consecutive nodes with the same values.

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
            prev = node
        node = node.next

def space_efficient(head: Node):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:  # THAT LITTLE ELSE, CHANGES EVERYTHING
                runner = runner.next   # Note: It is actually this assignment (because it is only here) that allows the algorithm to `jump` consecutive nodes that were already seen
        current = current.next

# TODO: I stopped there to think of a small issue: why is node set to node.next at the end of the simple() function. Why not prev.next?
# The same goes for current that would have been set to current.next instead of runner.next?
# My current thoughts are the following: First, in simple(), there is no inner loops, so no nodes could really be `jumped`. For space_efficient(), because current and runner referenced the same object, if runner changes the sequence of nodes in the LL, the will also be changed for current.
# Thus, if runner `removes` or `jumps` a node, it will also disappear for current. So for the list 1, 2, 2, 2, 3, current will only see a single 2.


head = Node(0)
current = head
for i in [1, 2, 2, 2, 2,  2, 2, 2, 2, 2,  2, 3]:
    new_node = Node(i)
    current.next = new_node
    current = new_node


space_efficient(head)


current = head
while current:
    print(current.data, end=" --> ")
    current = current.next
