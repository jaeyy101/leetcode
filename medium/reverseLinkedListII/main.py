from utils.linkedlist import Node, LinkedList


class Solution:
    def reverseBetween(self, head: Node, left: int, right: int) -> Node:
        count = 1
        curr = head
        start = None

        while curr:
            # Iterate until the current node is the start point
            if left == count:

                # Make a new head and a previous node
                new_head = curr
                prev = curr

                # Iterate through list till we reach end point
                while curr and count <= right:

                    # Keep track of next value
                    next = curr.next

                    # Make current node point to head
                    curr.next = new_head

                    # Make previous/pivot node point to the next
                    prev.next = next

                    # Make the current node the new head
                    new_head = curr
                    curr = next
                    count += 1
                if not start:
                    head = new_head
                else:
                    start.next = new_head
                break
            count += 1
            start = curr
            curr = curr.next

        return head

    def reverseBetween1(self, head: Node, left: int, right: int) -> Node:
        if not head or left == right:
            return head

        dummy = Node(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next


s = LinkedList()
for i in range(5, 0, -1):
    s.add(i)

res = Solution().reverseBetween1(s.head, 1, 5)
while res:
    print(res.val)
    res = res.next
