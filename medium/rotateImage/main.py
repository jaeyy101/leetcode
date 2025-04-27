class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Rotate the matrix 90 degrees clockwise in-place
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                for pair in [
                    (i, j),
                    (j, n - i - 1),
                    (n - i - 1, n - j - 1),
                    (n - j - 1, i),
                ]:
                    print(pair)
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = temp

        print(matrix)


# print(
#     Solution().rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
# )
print(Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
