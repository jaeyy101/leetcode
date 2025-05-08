class Solution:
    def rotateRight(self, head: Node, k: int) -> Node:
        if not head:
            return None
        temp = head

        n = 1
        while temp.next:
            n += 1
            temp = temp.next

        k = k % n
        if not k:
            return head

        fast, slow = head, head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        new_head = slow.next
        slow.next = None
        fast.next = head

        return new_head
