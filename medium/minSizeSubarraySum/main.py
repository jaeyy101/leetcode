class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        end = 1
        n = len(nums)

        current_total = nums[start]
        smallest_sum_len = 0
        while end <= n:
            if current_total >= target:
                if smallest_sum_len == 0:
                    smallest_sum_len = end - start
                else:
                    smallest_sum_len = min(smallest_sum_len, end - start)

            if current_total < target:
                if end >= n:
                    break
                current_total += nums[end]
                end += 1
            else:
                current_total -= nums[start]
                start += 1

        return smallest_sum_len

    def prefixSum(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        def binary_search(left, right, key):
            while left < right:
                mid = (left + right) // 2
                if prefix[mid] < key:
                    left = mid + 1
                else:
                    right = mid
            return left

        min_len = float("inf")

        for i in range(n):
            to_find = prefix[i] + target
            bound = binary_search(i + 1, n + 1, to_find)
            if bound <= n:
                min_len = min(min_len, bound - i)

        return 0 if min_len == float("inf") else min_len


print(Solution().prefixSum(11, [1, 2, 3, 6, 5]))
