R"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""


# To account for most cases, we will solve for:
# 1. When the LL is Singly Linked: We have to receive the head.
# 2. When it is Doubly Linked (to make it interesting we will not expect to necessarily receive the head but any node).
# 3. When it is doubly linked and circular
class NodeSinglyLinked:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class NodeDoublyLinked:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def with_buffer_singly_linked(head: NodeSinglyLinked):
    n = head
    s = n.next
    l = [n.data]
    while n and s:
        while s.data in l:
            s = s.next
        else:
            l.append(s.data)
            n.next = s
            n = s
            s = n.next
    return head


def with_buffer_doubly_linked(n: NodeDoublyLinked):
    while n.prev:
        n = n.prev

    head = n
    s = n.next
    l = [n.data]
    while n and s:
        if s.data in l:
            n.next = s.next
        else:
            l.append(s.data)
        n = s
        s = n.next

    return head


def with_buffer_circular(node: NodeDoublyLinked):
    pass


def remove_dups_with_buffer(head_node):
    R"""
    Implementing this in python might not be as intuitive as it would in c/c++.
    We assume the nodes are references. Also, we used a dict instead of a hash_table.
    """
    n = head_node

    d = {head_node.data: True}

    while n.next:  # != None:
        if n.next.data in d.keys():
            n.next = n.next.next
        else:
            d[n.next.data] = True
        n = n.next

    return head_node  # if head is duplicated, it is indeed its duplicate that will be deleted, we won't modify head


def remove_dups(head_node):
    def remove_subs_dups(start):
        n = start
        while n.next:
            if n.next.data == start.data:  # We cannot simply use `is` here. The instances are different, they just
                # contain same data
                n.next = n.next.next
                # We do not return here because there might be more duplicates down the road
            n = n.next

    n = head_node
    while n and n.next:
        remove_subs_dups(n)
        n = n.next


def print_ll(head):
    while head:
        print(head.data)
        head = head.next  # head is not subsequently used


a = [1, 2, 3, 4, 1, 4, 6, 7]
node = head = NodeSinglyLinked(0)
for i in a:
    n = NodeSinglyLinked(i)
    node.next = n
    node = n

head = with_buffer_singly_linked(head)
print_ll(head)
