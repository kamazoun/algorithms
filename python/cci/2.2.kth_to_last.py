R'''
 Implement an algorithm to find the kth to last element of a singly linked list.
'''



def kth_to_last(head, k):
    R'''
    O(n) time and O(1) space.
    '''
    if not head:
        return None

    n = head
    while k > 0 and n:
        n = n.next
        k -= 1
    if not n.next:
        return n

    m = head
    while n.next:
        n = n.next
        m = m.next

    return m
