class Solution:
    def rob(self, nums: list[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dp(i + 2), dp(i + 1))

        return dp(0)


print(Solution().rob([2, 1, 1, 2]))
