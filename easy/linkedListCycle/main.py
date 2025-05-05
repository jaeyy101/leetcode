import random
from utils.linkedlist import LinkedList, Node


class Solution:
    def hasCycle(self, head: Node):
        if not head:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False


# s = LinkedList()
# nums = [1, 2, 4, 5, 6, 9, 14]
# cycle = random.choice(nums)
# s.add(12)
# tail = s.head

# for num in nums:
#     s.add(num)
#     if cycle == num:
#         tail.next = s.head
