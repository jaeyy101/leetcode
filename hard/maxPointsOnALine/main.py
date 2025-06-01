from collections import defaultdict
import math


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        res = 0
        slopes_and_intercepts = defaultdict(int)
        for i in range(n - 1):
            for j in range(i + 1, n):
                den, num = points[j][0] - points[i][0], points[j][1] - points[i][1]
                if den:
                    slope = num / den
                    y_intercept = points[i][1] - slope * points[i][0]
                else:
                    slope = f"h{points[j][0]}"
                    y_intercept = 0
                slopes_and_intercepts[(slope, y_intercept)] += 1
                res = max(res, slopes_and_intercepts[(slope, y_intercept)])
        return int((1 + math.isqrt(1 + 8 * res)) / 2)

    def maxPoints1(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        res = 0
        for i in range(n - 1):
            x_1, y_1 = points[i]
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                x_2, y_2 = points[j]
                den, num = x_2 - x_1, y_2 - y_1
                if den:
                    slope = num / den
                else:
                    slope = float("inf")
                slopes[slope] += 1
                res = max(res, slopes[slope])
        return res + 1


print(Solution().maxPoints1([[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]))
