class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(i, target):
            if target == 0:
                res.append(path[:])
                return

            for j in range(i, len(candidates)):
                candidate = candidates[j]
                if candidate <= target:
                    path.append(candidate)
                    backtrack(j, target - candidate)
                    path.pop()

        backtrack(0, target)
        return res
