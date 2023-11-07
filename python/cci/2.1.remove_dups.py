R"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

def remove_dups_with_buffer(head_node):
    R"""
    Implementing this in python might not be as intuitive as it would in c/c++.
    We assume the nodes are references. Also we used a dict instead of a hash_table.
    """
    n = head_node

    dict = {}
    d[head_node.data] = True

    while n.next: # != None:
        if n.next.data in dict.keys():
            n.next = n.next.next
        else
            d[n.next.data] = True
        n = n.next

    return head_node # if head is duplicated, it is indeed its duplicate that will be deleted, we won't modify head

def remove_dups(head_node):

    def remove_subs_dups(start):
        n = start
        while n.next:
            if n.next.data == start.data: # We cannot simply use `is` here. The instances are different, they just contain same data
                n.next = n.next.next
                # We do not return here because there might be more duplicates down the road
            n = n.next

    n = head_node
    while n and n.next:
        remove_subs_dups(n)
        n = n.next
