class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                alive_neighbors = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n and (x != i or y != j):
                            if abs(board[x][y]) == 1:
                                alive_neighbors += 1

                if board[i][j] == 1:
                    if not 2 <= alive_neighbors <= 3:
                        board[i][j] = -1
                else:
                    if alive_neighbors == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

        print(board)


Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
