from utils.linkedlist import Node, LinkedList


class Solution:
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        first_pointer = l1
        second_pointer = l2

        head = None
        tail = None
        carry_over = 0
        while first_pointer or second_pointer or carry_over:
            val1 = first_pointer.val if first_pointer else 0
            val2 = second_pointer.val if second_pointer else 0

            total = val1 + val2 + carry_over
            carry_over = total // 10

            node = Node(total % 10)
            if head:
                tail.next = node
                tail = node
            else:
                head = node
                tail = node

            first_pointer = first_pointer.next if first_pointer else None
            second_pointer = second_pointer.next if second_pointer else None

        return head
