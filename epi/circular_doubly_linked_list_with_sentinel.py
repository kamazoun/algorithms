
class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self) -> str:
        return f'Node(data={self.data})'

class LinkedList:
    def __init__(self):
        self._sentinel = Node(data=None)
        self._sentinel.next = self._sentinel
        self._sentinel.prev = self._sentinel

    def pop_left(self) -> Node:
        return self.remove_by_ref(self._sentinel.next)

    def pop(self) -> Node:
        return self.remove_by_ref(self._sentinel.prev)

    def append_nodeleft(self, node):
        self.add_node(self._sentinel, node)

    def append_node(self, node):
        self.add_node(self._sentinel.prev, node)

    def append_left(self, data):
        node = Node(data=data)
        self.append_nodeleft(node)

    def append(self, data):
        node = Node(data=data)
        self.append_node(node)

    def remove_by_ref(self, node) -> Node:
        if node is self._sentinel:
            raise Exception('Can never remove sentinel.')
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node

    def add_node(self, curnode, newnode):
        newnode.next = curnode.next
        newnode.prev = curnode
        curnode.next.prev = newnode
        curnode.next = newnode

    def search(self, value):
        self._sentinel.data = value
        node = self._sentinel.next
        while node.data != value:
            node = node.next
        self._sentinel.data = None
        if node is self._sentinel:
            return None
        return node

    def __iter__(self):
        node = self._sentinel.next
        while node is not self._sentinel:
            yield node.data
            node = node.next

    def reviter(self):
        node = self._sentinel.prev
        while node is not self._sentinel:
            yield node.data
            node = node.prev

ll = LinkedList()
n = Node(17)
ll.append_node(n)
print(ll)
