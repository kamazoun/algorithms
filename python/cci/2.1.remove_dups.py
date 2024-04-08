R"""
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""


class NodeSinglyLinked:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data: int):
        node = NodeSinglyLinked(data)
        if self.head is None:
            self.head = node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = node

    def remove_dups_simple(self):
        pass

    def remove_dups_efficient(self):
        pass

# TODO: simple idea: why not implement the remove function in each class: for instance NodeSinglyLinked could have a remove method that removes the duplicated node and NodeDoublyLinked could also have a remove method. They could all even have multiple methods for `with buffer` and `without buffer`.
# The issue is that right now, NodeSinglyLinked and NodeDoublyLinked represent nodes, so we would need to either adapt them or create entirely new classes to represent the linked lists.


# To account for most cases, we will solve for:
# 1. When the LL is Singly Linked: We have to receive the head.
# 2. When it is Doubly Linked (to make it interesting we will not expect to necessarily receive the head but any node).
# 3. When it is doubly linked and circular

class NodeDoublyLinked:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


def with_buffer_singly_linked(head: NodeSinglyLinked):
    R"""
    :param head: The head node of the Linked list
    :return: returns the same head because there is no way the head would change

    :idea: We use a running pointer to find if a node's data is already in the list, otherwise we add it to the list.
    If a node is duplicated, we point the slow pointer to the first pointer after the fast pointer that is not
    duplicated (its data is not in the list). To accomplish this, we use the while...else construct.
    """
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


def with_buffer_doubly_linked_simple(n: NodeDoublyLinked):
    while n.prev:
        n = n.prev

    head = n
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
    R"""
    :param n: Any node, does not need to be the head.
    :return: The head. Can be different from the received node

    :idea: Here there are different ways to go about it. If there is no particular restriction on how to select the
    duplicated nodes that are to be removed, we do not need to first `reverse` to find the head. We can simply save
    the node n, and from there go forward and go backward to eliminate the duplicates. How would it be done?
    * The value of n is duplicated in the LL:
     ** The node before and after n hold the same value as n: By intuition, it feels better to first go backward (
     although in the doubly LL, backward and forward are relative) from n (the nodes before n that hold the same
     value as n will point to n.next). Then we will keep a variable pointing to the first not deleted node before n,
     so that if n is deleted, that node will point to the first not deleted node after n. We might also want to save
     the head node when found.

    * The value of n is not duplicated in the LL: We follow a process similar to what is described above,
    but as we do not know beforehand if n is duplicated, we use the same algorithm to find out.
    """
    fbn = n.prev # first_before_n. I should not need to keep that because it should be accessible via n.prev
    current = n.prev
    l = [n.data]
    head = None

    while current:
        if current.data in l:
            t = current.prev
            while t.data in l:
                t = t.prev
            current.prev = t
        else:
            l.append(current.data)
        head = current
        current = current.prev
    current = n
    while current:
        if current.data in l:
            t = current.next
            while t and t.data in l:
                t = t.next
            current.next = t
        else:
            l.append(current.data)
        current = current.next

    return head

    # while current.prev:
    #     if current.prev.data not in l:
    #         current.prev.next = current
    #         l.append(current.prev.data)
    #     else:
    #         while current.prev and current.prev.data in l:
    #             current = current.prev
    # head = current
    # current = n.prev
    # while current and current.next:
    #     if current.next.data in l:
    #         current.next = current.next.next
    #     else:
    #         l.append(current.next.data)
    #     current = current.next
    # return head
    #


def with_buffer_circular(node: NodeDoublyLinked):
    R"""
    The trick here will be to know when a cycle is completed
    :param node: Any node of the LL
    :return: Any node
    """
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


def print_multill(head1, head2, head3):
    while head1 and head2 and head3:
        print(f'{head1.data} \t {head2.data} \t {head3.data}')
        head1 = head1.next  # head is not subsequently used
        head2 = head2.next
        head3 = head3.next


a = [1, 2, 3, 4, 1, 4, 6, 7]
# node = head = NodeSinglyLinked(0)
# for i in a:
#     n = NodeSinglyLinked(i)
#     node.next = n
#     node = n
#
# head = with_buffer_singly_linked(head)
# #print_ll(head)


node = head = NodeDoublyLinked(0)
for i in a:
    n = NodeDoublyLinked(i)
    n.prev = node
    node.next = n
    node = n
#
# head1 = with_buffer_doubly_linked(node)
# head2 = with_buffer_doubly_linked(node.prev.prev)
# head3 = with_buffer_doubly_linked(head)
# print_multill(head1, head2, head3)


def remove_duplicates(node: NodeDoublyLinked):
    seen = {node.data}
    # Remove duplicates after the node
    current = node.next
    while current:
        if current.data in seen:
            # Remove the node
            if current.next:
                current.next.prev = current.prev
            current.prev.next = current.next
        else:
            seen.add(current.data)
        current = current.next

    # Remove duplicates before the node
    head = None
    current = node.prev
    while current:
        if current.data in seen:
            # Remove the node
            if current.prev:
                current.prev.next = current.next
            current.next.prev = current.prev
        else:
            seen.add(current.data)
        current = current.prev
        if current: head = current
    return head

# head1 = remove_duplicates(node)
# head2 = remove_duplicates(node.prev.prev)
# head3 = remove_duplicates(head)
# print_multill(head1, head2, head3)