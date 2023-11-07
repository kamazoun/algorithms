R'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''



def partition(head: LinkedListNode, x: int):
    R'''
    Mine: I had forgotten to return head.
    '''
    if not head:
        return head

    left = middle = right = None
    node = head

    while node:
        if node.data < x:
            if left:
                left.next = node
            else:
                head = node
            left = node
        else:
            if not middle:
                middle = node
            else:
                right.next = next
            right = node
    if left:
        left.next = middle
        return head
    else:
        return middle
 # Author's just uses two nodes head and tail and append before head and after tail
