# Definition for singly-linked list.
class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - the value and next node in list
    """

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"<Node data: {self.value}>"


class Solution:
    def isPalindrome(self, list: Node) -> bool:
        head = list
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        left_list = head
        right_list = slow.next
        slow.next = None

        reversed_right_head = self.reverseList(right_list)

        while left_list and reversed_right_head:
            if left_list.value != reversed_right_head.value:
                return False
            left_list = left_list.next
            reversed_right_head = reversed_right_head.next

        return True

    def reverseList(self, head: Node):
        prev = None
        current = head
        next = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


def print_list(head: Node):
    if head == None:
        print(head)
        return

    print(f"[Head: {head.value}]", end="")
    if head.next is not None:
        temp = head.next
        print("->", end="")
        while temp:
            if temp.next == None:
                print(f"[Tail: {temp.value}]", end="")
            else:
                print(f"[{temp.value}]->", end="")
            temp = temp.next
    print()


def main():
    head = Node(1)
    first = Node(1)
    middle = Node(2)
    last = Node(1)

    head.next = first
    first.next = middle
    middle.next = last

    print_list(head)
    test = Solution()
    print(test.isPalindrome(head))


if __name__ == "__main__":
    main()
