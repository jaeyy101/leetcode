class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def get_row_and_col(num):
            return num // n, num % n

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            r, c = get_row_and_col(mid)

            print(matrix[r][c])
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
