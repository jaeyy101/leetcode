class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # Performs a deep copy on a linked list and all it's attributes

        if not head:
            return None

        # Make old nodes point at new ones
        curr = head
        while curr:
            # Create new node for each old one
            new_node = Node(curr.val)
            # Make the new node point to rest of list
            new_node.next = curr.next
            # Point the old node to the new one
            curr.next = new_node
            # Push
            curr = curr.next.next

        # Each old node now has the new clone next to it.
        # Using this logic to attach random attribute
        curr = head
        while curr:
            random_node = curr.random
            if random_node:
                curr.next.random = random_node.next
            curr = curr.next.next

        # Now removing the original linked list
        head = head.next
        curr = head
        while curr and curr.next:
            to_be_removed = curr.next
            curr.next = to_be_removed.next
            to_be_removed.next = None
            curr = curr.next

        return head


s = LinkedList()
s.add(2)
s.add(3)
s.add(4)

curr = Solution().copyRandomList(s.head)
while curr:
    print(curr.val)
    curr = curr.next
