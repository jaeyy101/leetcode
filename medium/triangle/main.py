class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        table = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                table[j] = triangle[i][j] + min(table[j], table[j + 1])
        print(table)
        return table[0]
