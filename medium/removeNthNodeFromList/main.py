from utils.linkedlist import Node, LinkedList


class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        # Start from head and move fast pointer by n places
        fast = head
        for _ in range(n):
            fast = fast.next

        # Dummy node for handling edge cases
        dummy = Node(0)
        dummy.next = head

        # Setting slow to dummy so we always end up one node before
        # nth node from end
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node
        slow.next = slow.next.next
        return dummy.next


s = LinkedList()
for i in range(1, 2):
    s.add(i)

res = Solution().removeNthFromEnd(s.head, 1)
while res:
    print(res.val)
    res = res.next
