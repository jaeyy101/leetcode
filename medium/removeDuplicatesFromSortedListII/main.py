class Solution:
    def deleteDuplicates(self, head: Node) -> Node:
        dummy = Node(0)
        dummy.next = head
        slow = dummy
        fast = slow.next

        while fast and fast.next:
            if slow.next.val < fast.next.val:
                slow = slow.next
                fast = fast.next
            else:
                # Once we meet a duplicate, iterate until it's no more
                num = fast.next.val
                while fast.next and num == fast.next.val:
                    fast = fast.next
                slow.next = fast.next
                fast = fast.next

        return dummy.next
