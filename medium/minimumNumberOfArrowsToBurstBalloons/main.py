# After
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0

        points.sort(key=lambda x: x[1])
        print(points)
        lower_bound, upper_bound = points[0]

        count = 0
        for i in range(1, n):
            current_low, current_high = points[i]
            if lower_bound <= current_low <= upper_bound:
                lower_bound = max(lower_bound, current_low)
                upper_bound = min(upper_bound, current_high)
            else:
                lower_bound = current_low
                upper_bound = current_high
                count += 1
        count += 1
        return count

    def findMinArrowShots1(self, points: list[list[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0

        points.sort(key=lambda x: x[1])

        res = 1
        bound = points[0]

        for i in range(1, n):
            point = points[i]
            if point[0] > bound[1]:
                bound = point
                res += 1

        return res


print(
    Solution().findMinArrowShots1(
        [
            [3, 9],
            [7, 12],
            [3, 8],
            [6, 8],
            [9, 10],
            [2, 9],
            [0, 9],
            [3, 9],
            [0, 6],
            [2, 8],
        ]
    )
)
