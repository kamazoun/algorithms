R"""
Let's try creating some classes for linked lists that should solve usual linked list problems
"""


class Node1:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedListWithNode:
    def __init__(self, node: Node1):
        self.head = node

    def get_data(self):
        return self.head.data

    def get_head(self):
        return self.head

    def get_tail(self):
        node = self.head
        while node.next:
            node = node.next
        return node

    def get_node_with_data(self, data):
        R"""
        :param data: The data that the returned node should contain
        :return: The first node containing the data or None
        """
        node = self.head
        while node and node.data != data:
            node = node.next

        return node
