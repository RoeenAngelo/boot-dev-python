from node import Node


class LinkedList:
    def add_to_head(self, node):
        node.set_next(self.head)
        if self.head is None:
            self.tail = node
        self.head = node

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.head = None
        self.tail = None