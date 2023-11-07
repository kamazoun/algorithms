R'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''


def del_middle_node(middle):
    if middle.next: #Should be true,as middle is not tail. If middle could be tail, we can set to none or a dummy or sentinel. Should point that out to interviewer.
        middle = middle.next

    '''
    Same as:
    middle.data = middle.next.data
    middle.next = middle.next.next
    '''
