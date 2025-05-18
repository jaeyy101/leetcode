class UnionFind:
    def __init__(self, N: int) -> None:
        self.p = list(range(N))

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n + 1)
        dummy = m * n

        def idx(r: int, c: int) -> int:
            return r * n + c

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    if r in (0, m - 1) or c in (0, n - 1):
                        uf.union(idx(r, c), dummy)
                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                            uf.union(idx(r, c), idx(nr, nc))

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and uf.find(idx(r, c)) != uf.find(dummy):
                    board[r][c] = "X"

        print(board)


print(
    Solution().solve(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "O"],
            ["X", "O", "X", "O"],
            ["X", "O", "X", "X"],
        ]
    )
)
