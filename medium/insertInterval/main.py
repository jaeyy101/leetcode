class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        overlap_start, overlap_end = newInterval

        res = []
        i = 0
        while i < n + 1:
            if i == n:
                res.append([overlap_start, overlap_end])
                break

            if overlap_start <= intervals[i][1]:
                start = min(overlap_start, intervals[i][0])
                end = overlap_end
                while i < n and intervals[i][0] <= end:
                    end = max(end, intervals[i][1])
                    i += 1
                res.append([start, end])
                break
            res.append(intervals[i])
            i += 1

        while i < n:
            res.append(intervals[i])
            i += 1

        return res


print(Solution().insert([[3, 5], [6, 7], [8, 10], [12, 16]], [11, 20]))
