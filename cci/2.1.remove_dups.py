R'''
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

def remove_dups_with_buffer(head_node):
    R'''
    Implementing this in python might not be as intuitive as it would in c/c++.
    We assume the nodes are references. Also we used a dict instead of a hash_table although
    '''
    n = head_node

    dict = []
    d[head_node.data] = True

    while n.next != None:
        if n.next.data in dict.keys():
            n.next = n.next.next
        else
            d[n.next.data] = True
        n = n.next

    return head_node # if head is duplicated, its duplicate will be deleted, we won't modify head
        
