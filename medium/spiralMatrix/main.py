class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        total = n * m

        count = 0
        cutback = 0
        res = []
        while count < total:
            i = cutback
            while count < total and i < m - cutback:
                res.append(matrix[cutback][i])
                count += 1
                i += 1

            i = cutback + 1
            while count < total and i < n - cutback:
                res.append(matrix[i][m - cutback - 1])
                count += 1
                i += 1

            i = m - cutback - 2
            while count < total and i >= cutback:
                res.append(matrix[n - cutback - 1][i])
                count += 1
                i -= 1

            i = n - cutback - 2
            while count < total and i >= cutback + 1:
                res.append(matrix[i][cutback])
                count += 1
                i -= 1

            cutback += 1

        return res


print(
    Solution().spiralOrder(
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
        ]
    )
)
