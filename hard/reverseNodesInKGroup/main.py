from utils.linkedlist import LinkedList, Node


class Solution:
    def reverseKGroup(self, head: Node, k: int) -> Node:
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        curr = prev.next

        while curr:
            for _ in range(k - 1):
                # A canceled out reverse if the current group length < k
                if not curr.next:
                    curr = prev.next
                    while curr.next:
                        temp = curr.next
                        curr.next = temp.next
                        temp.next = prev.next
                        prev.next = temp
                    break
                # Reverse current group
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            prev = curr
            curr = curr.next
        return dummy.next


s = LinkedList()
for i in range(10, 0, -1):
    ...

res = Solution().reverseKGroup(s.head, 4)
while res:
    print(res.val)
    res = res.next
