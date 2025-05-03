import bisect


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

    def insert1(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        starts = [interval[0] for interval in intervals]
        ends = [interval[1] for interval in intervals]

        left = bisect.bisect_left(ends, newInterval[0])
        right = bisect.bisect_right(starts, newInterval[1])

        if left < right:
            new_left = min(newInterval[0], intervals[left][0])
            new_right = max(newInterval[1], intervals[right - 1][1])
            newInterval = [new_left, new_right]

        return intervals[:left] + [newInterval] + intervals[right:]


print(Solution().insert1([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 7]))
