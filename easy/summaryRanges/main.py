class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n = len(nums)
        res = []

        i = 0
        while i < n:
            start = nums[i]
            while i < n - 1 and nums[i + 1] - nums[i] == 1:
                i += 1
            end = nums[i]
            res.append(f"{start}->{end}" if start != end else str(start))
            i += 1

        return res


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
