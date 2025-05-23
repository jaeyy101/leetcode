from functools import lru_cache


class Solution:
    def noOfWays(self, m, n, x):
        @lru_cache(maxsize=None)
        def dp(i, target) -> int:
            if i == n:
                return 1 if target == 0 else 0

            res = 0
            for j in range(1, m + 1):
                if not j <= target:
                    break
                res += dp(i + 1, target - j)

            return res

        return dp(0, x)


print(Solution().noOfWays(10, 9, 100))
