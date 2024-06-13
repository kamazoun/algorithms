R'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

from node import Node


"""
After reading my initial solution of a few years back, I noticed that this question, for the singly LL case, is quite language dependent: what is passed to the function? A reference to the node? a pointer?
If `middle` is a pointer (memory address), indeed we could simply replace it with the value of the next node's address. What if the previous node only stores the reference of the next node? For instance in Python, we may need to change that next pointer to hold the value of the next.next node. How do we do that without access to head?
I also read an article on Medium recently that explained the way Python deals with references in memory. I think I will have to dive deeper in this before coming back.

To keep the code clean, I will include the explanation and reasoning in the file containing the node class.

Here let's try to implement 2 solutions:
1. Following the reasoning above, we should be able to replace the memory address for the node to delete with its next node. In that case if next is None, we should be able to replace with None.
2. Following author's solution, we can replace the fields within the node.
"""

# TODO


def delete_middle_node(middle: Node) -> None:
    pass

def delete_middle_node_author(middle: Node) -> bool:
    if not middle or not middle.next:
        return False
    middle.data = middle.next.data
    middle.next = middle.next.next
    return True


def del_middle_node(middle):
    if middle.next: #Should be true,as middle is not tail. If middle could be tail, we can set to none or a dummy or sentinel. Should point that out to interviewer.
        middle = middle.next
    '''
    Same as:
    middle.data = middle.next.data
    middle.next = middle.next.next
    '''

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

#delete_middle_node_author(node2)
current = node1
node2 = node3
while current:
    print(current.data, end=" --> ")
    current = current.next