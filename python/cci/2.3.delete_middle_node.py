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
As I am preparing for this challenge, I refactored Node into a single file.
To make the challenge interesting, we will solve for doubly linked and singly linked.
For singly, I think I made an error previously, because the previous node needs to point to the next one. If there is no repeating elements, then starting from the head we can easily find the previous node.
"""


"""
After reading my initial solution of a few years back, I noticed that this question, for the singly LL case, is quite language dependent: what is passed to the function? A reference to the node? a pointer?
If `middle` is a pointer (memory address), indeed we could simply replace it with the value of the next node's address. What if the previous node only stores the reference of the next node? For instance in Python, we may need to change that next pointer to hold the value of the next.next node. How do we do that without access to head?
I also read an article on Medium recently that explained the way Python deals with references in memory. I think I will have to dive deeper in this before coming back.
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
