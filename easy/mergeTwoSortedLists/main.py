from utils.linkedlist import Node, LinkedList


class Solution:
    def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
        fp = list1
        sp = list2

        head = None
        tail = None
        while fp or sp:
            val1 = fp.val if fp else float("inf")
            val2 = sp.val if sp else float("inf")
            if val1 < val2:
                node = Node(val1)
                fp = fp.next
            else:
                node = Node(val2)
                sp = sp.next

            if head:
                tail.next = node
                tail = node
            else:
                head = node
                tail = node

        return head


s = LinkedList()

t = LinkedList()

res = Solution().mergeTwoLists(s.head, t.head)
while res:
    print(res.val)
    res = res.next
