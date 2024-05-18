R'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

from node import Node


"""
As I am preparing for this challenge, I refactored Node into a single file.
To make the challenge interesting, we will solve for doubly linked and singly linked.
For singly, I think I made an error previously, because the previous node needs to point to the next one. If there is no repeating elements, then starting from the head we can easily find the previous node.
"""

def delete_middle_node(node: None) -> Node:
    pass

def del_middle_node(middle):
    if middle.next: #Should be true,as middle is not tail. If middle could be tail, we can set to none or a dummy or sentinel. Should point that out to interviewer.
        middle = middle.next

    '''
    Same as:
    middle.data = middle.next.data
    middle.next = middle.next.next
    '''
