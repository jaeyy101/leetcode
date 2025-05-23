class Node:
    def __init__(self, value=None):
        self.val = value
        self.next: Node = None
        self.random: Node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
