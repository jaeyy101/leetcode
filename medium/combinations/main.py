class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(i):
            if len(path) == k:
                res.append(path[:])
                return

            for j in range(i, n + 1):
                path.append(j)
                backtrack(j + 1)
                path.pop()

        backtrack(1)
        return res


print(Solution().combine(4, 2))
