# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def mergeSort(left, right):
            if not left < right:
                return lists[left]

            mid = (left + right) // 2

            left_list = mergeSort(left, mid)
            right_list = mergeSort(mid + 1, right)

            return merge(left_list, right_list)

        def merge(left, right):
            dummy = ListNode(0)
            curr = dummy
            while left and right:
                if left.val < right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            curr.next = left if left else right
            return dummy.next

        return mergeSort(0, len(lists) - 1)

    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        counter = count()
        heap = []
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(heap, (curr.val, next(counter), curr))
                curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        while heap:
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next
        return dummy.next
