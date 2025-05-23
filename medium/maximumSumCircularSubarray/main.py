class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> float:
        max_sum = float("-inf")
        current_max = 0
        min_sum = float("inf")
        current_min = 0
        total = 0

        for num in nums:
            current_max += num
            max_sum = max(max_sum, current_max)
            current_min += num
            min_sum = min(min_sum, current_min)
            if current_max < 0:
                current_max = 0
            if current_min > 0:
                current_min = 0
            total += num

        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
