from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)
        if any(word_count[c] > board_count[c] for c in word_count):
            return False

        m = len(board)
        n = len(board[0])

        def backtrack(r, c, i):
            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True

            board[r][c] = "#"  # Mark visited

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if backtrack(nr, nc, i + 1):
                        return True

            board[r][c] = word[i]
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
