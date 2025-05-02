class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        res = []
        start, end = intervals[0]

        for i in range(1, n):
            curr_start, curr_end = intervals[i]
            if curr_start <= end:
                end = max(end, curr_end)
            else:
                res.append([start, end])
                start, end = curr_start, curr_end

        res.append([start, end])
        return res


print(Solution().merge([[1, 4], [0, 4]]))
