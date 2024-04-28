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

    def remove_dups_efficient_from_node(self, node: NodeSinglyLinked):
        """
        Note: Practically there is no need to do that if the LL is not circular, because even if we start at a node, we will also need to restart at the head in order to complete the full LL as, there is no `prev` link to go backwards.
        So, I will work on this method with the assumption that the list is circular.
        One aspect to test when the list is circular, is how it behaves for a single pointing to itself.
        That also leads me to question the algorithm that should decide of the length of the list, because is the list has a unique node that points to itself, it should be a circular ll of length one. But if it has 2 nodes with the same data, it should be a circular ll of length 2.
        I guess, we can approach the problem, considering any number of adjacent nodes with the same value as 1 node.
        For instance 1 -> 1 -> 1 -> 2 -> 1 -> 2 -> 2 -> 3 would give 1 -> 2 -> 1 -> 2 -> 3.
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


class NodeDoublyLinked:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.prev.data}<----{self.data}----->{self.next}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def _traverse(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    def add_node(self, data: int, position: int = -1):
        r"""
        Because this is not the challenge here, I will not add methods to add nodes at the start and end of the LL.
        """
        new_node = NodeDoublyLinked(data)
        if self.head is None:
            self.head = new_node
            return None
        if position == -1:
            # Add at the end
            end = self._traverse()
            end.next = new_node
            new_node.prev = end
            return new_node
        else:
            if position < 0:
                return None # Edge case
            elif position == 0:
                pass
                # Decide what to do, change the head? Replace it?
            else:
                pass
                # Here manually traverse, pay attention to check the length of the LL not to go beyond

    def remove_dups_simple(self):
        seen = []
        current = self.head
        while current:
            if current.data in seen:
                current.prev.next = current.next # Because the head will not be in the list at first, current.prev will NEVER be None.\
                if current.next is not None:
                    current.next.prev = current.prev
            else:
                seen.append(current.data)
            current = current.next
        return self.head

    def remove_dups_efficient(self):
        current = self.head
        while current:
            runner = current.next
            while runner:
                if runner.data == current.data:
                    runner.prev.next = runner.next
                    if runner.next:
                        runner.next.prev = runner.prev
                runner = runner.next
            current = current.next
        return self.head

    def remove_dups_efficient_circular(self):
        pass

    def remove_dups_efficient_from_node(self, node: NodeDoublyLinked):
        """
        Note: here we won't necessarily receive the head.
        We need to check forward and backwards from the node.
        We could use a list to keep track of the node seen, otherwise we would need to go from end to end checking if a node is duplicated, which is what we will do to try making it more challenging.
        """
        # TODO: The code has an error in the backwards implementation and also struggles with deepcopy error. (current becomes None and so does node)
        current_prev, current_next = node, node
        # Removing duplicates backwards from current_prev
        while current_prev:
            prev_node = current_prev.prev
            while prev_node:
                if prev_node.data == current_prev.data:
                    if prev_node.prev:
                        prev_node.prev.next = current_prev
                    current_prev.prev = prev_node.prev
                prev_node = prev_node.prev
            current_prev = current_prev.prev

        # Removing duplicates forward from current_next
        while current_next:
            runner = current_next.next
            while runner:
                if runner.data == current_next.data:
                    runner.prev.next = runner.next
                    if runner.next:
                        runner.next.prev = runner.prev
                runner = runner.next
            current_next = current_next.next
        return self.head

    def __repr__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return "<->".join(result)


dll = DoublyLinkedList()
node = dll.add_node(1)
for i in [1, 2, 3, 3, 4, 1, 1]:
    dll.add_node(i)
print(dll)
dll.remove_dups_efficient_from_node(node)
# dll.remove_dups_simple()
print(dll)


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

