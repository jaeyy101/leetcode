from functools import lru_cache


class Solution:
    @lru_cache
    def climbStairsMemoization(self, n: int) -> int:
        if n in [0, 1]:
            return 1

        return self.climbStairsMemoization(n - 1) + self.climbStairsMemoization(n - 2)

    def climbStairsTabulation(self, n: int) -> int:
        table = [1, 1]
        for i in range(2, n + 1):
            table.append(table[i - 1] + table[i - 2])
        return table[n]

    def climbStairsStraight(self, n: int) -> int:
        prev, curr = 1, 1
        for _ in range(n - 1):
            prev, curr = curr, prev + curr
        return curr


print(Solution().climbStairsTabulation(30))
