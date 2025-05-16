from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def bfs(row, col):
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

        def dfs(r, c):
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
