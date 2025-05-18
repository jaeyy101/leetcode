from collections import deque


class UnionFind:
    def __init__(self, N: int) -> None:
        self.parent = list(range(N))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[rb] = ra


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(row: int, col: int):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0":
                    continue
                grid[r][c] = "0"
                queue.append((r + 1, c))
                queue.append((r, c - 1))
                queue.append((r - 1, c))
                queue.append((r, c + 1))

        def dfs(r: int, c: int):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == "0":
                return
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r - 1, c)
            dfs(r, c + 1)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans

    def numIslandsUnion(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def idx(r: int, c: int) -> int:
            return r * n + c

        uf = UnionFind(m * n)
        ans = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    for dr, dc in [(1, 0), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            uf.union(idx(r, c), idx(nr, nc))

        visited_group: "set[int]" = set()
        for r in range(m):
            for c in range(n):
                if grid[r][c] != "1":
                    continue
                parent = uf.find(idx(r, c))
                if parent not in visited_group:
                    visited_group.add(parent)
                    ans += 1
        return ans


print(Solution().numIslandsUnion([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
