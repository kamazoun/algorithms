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
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def remove_dups_simple(self):
        current = self.head
        prev = None
        seen = []
        while current:
            if current.data in seen:
                current = current.next
                prev.next = current  # prev will never be None here as at first step, seen will be empty
            else:
                seen.append(current.data)
                prev = current
                current = current.next


    def remove_dups_efficient(self):
        R"""
        The efficiency here refers to space. Time will increase to O(n^2).
        The solution will make use of a running pointer. There are 2 ways to move the running pointer:
        1. Make a second pointer `prev` or `first` that will, at each move of the `current` pointer, go from the `head` to the `current` pointer. The major issue with that solution would be finding the current pointer to stop the iteration of `prev` as we only use `int` to recognize nodes. Of course, if well implemented, no other value equal to `current.data` would be found twice on the path of `prev` until it reaches `current`.
        2. Make a second pointer `next` or `last` that will, at each move of `current`, go from the node after current until the end of the LL. The issue here is that we would need to keep track of a `prev` node that we would use to jump `current` if its data is not unique.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            is_seen = False
            while next_node:
                if next_node.data == current.data:
                    is_seen = True
                    break
                next_node = next_node.next
            if is_seen:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
            else:
                prev = current
            current = current.next





    def remove_dups_efficient_circular(self):
        """
        Note: here there won't be no head.
        """
        pass

    def __repr__(self):
        result = []
        head = self.head
        while head:
            result.append(str(head.data))
            head = head.next

        return '->'.join(result)

sll = SinglyLinkedList()
for i in [1, 2, 2, 3, 2, 1, 4, 1]:
    sll.add_node(i)
print(sll)
sll.remove_dups_efficient()
print(sll)
sll = SinglyLinkedList()
for i in [1, 1]:
    sll.add_node(i)
print(sll)
sll.remove_dups_efficient()
print(sll)



# To account for most cases, we will solve for:
# 1. When the LL is Singly Linked: We have to receive the head.
# 2. When it is Doubly Linked (to make it interesting we will not expect to necessarily receive the head but any node).
# 3. When it is doubly linked and circular

class NodeDoublyLinked:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    pass

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


def print_multill(head1, head2, head3):
    while head1 and head2 and head3:
        print(f'{head1.data} \t {head2.data} \t {head3.data}')
        head1 = head1.next  # head is not subsequently used
        head2 = head2.next
        head3 = head3.next


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