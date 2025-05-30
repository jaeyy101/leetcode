class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        queue = deque()
        carry = 1
        for digit in reversed(digits):
            total = digit + carry
            queue.appendleft(total % 10)
            carry = total // 10

        if carry:
            queue.appendleft(carry)

        return list(queue)
