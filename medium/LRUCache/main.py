class ListNode:
    def __init__(self, val):
        self.val = val
        self.key = None
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1

        self.move_node_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.map[key].val = value
            return self.move_node_to_head(node)

        node = ListNode(value)
        self.map[key] = node

        node.key = key
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

        if self.size == self.capacity:
            del self.map[self.tail.key]
            prev = self.tail.prev
            prev.next = None
            self.tail = prev
        else:
            if not self.tail:
                self.tail = node
            self.size += 1

    def move_node_to_head(self, node: ListNode) -> None:
        if node == self.head:
            return
        prev = node.prev
        next = node.next
        prev.next = next
        if next:
            next.prev = prev
        elif node == self.tail:
            self.tail = prev
        self.head.prev = node
        node.prev = None
        node.next = self.head
        self.head = node
