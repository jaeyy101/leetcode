class Solution:
    def partition(self, head: Node, x: int) -> Node:
        dummy = Node(0)
        dummy.next = head
        insertion_ptr, comparison_ptr = dummy, dummy

        while comparison_ptr.next:
            if comparison_ptr.next.val < x:
                if insertion_ptr == comparison_ptr:
                    insertion_ptr = insertion_ptr.next
                    comparison_ptr = comparison_ptr.next
                else:
                    node = comparison_ptr.next
                    comparison_ptr.next = node.next
                    node.next = insertion_ptr.next
                    insertion_ptr.next = node
                    insertion_ptr = node
            else:
                comparison_ptr = comparison_ptr.next

        return dummy.next
