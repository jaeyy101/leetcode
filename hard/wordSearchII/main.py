from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["end"] = word  # Store the full word at the end

        m, n = len(board), len(board[0])
        result = []

        def backtrack(x, y, parent):
            letter = board[x][y]
            cur_node = parent[letter]

            # Check if a word ends here
            if "end" in cur_node:
                result.append(cur_node["end"])
                del cur_node["end"]  # Avoid duplicates

            # Mark visited
            board[x][y] = "#"

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    next_char = board[nx][ny]
                    if next_char in cur_node:
                        backtrack(nx, ny, cur_node)

            # Restore cell
            board[x][y] = letter

            # Optimization: prune the Trie node if it's empty
            if not cur_node:
                del parent[letter]

        # Step 2: Start backtracking from each cell
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        print(trie)

        return result


print(
    Solution().findWords(
        [["a", "b"]],
        ["ab"],
    )
)
