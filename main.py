class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import lru_cache

        n = len(word1)
        m = len(word2)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == n and j == m:
                return 0

            # For inserting a character
            insert = float("inf")
            if j < m:
                insert = dp(i, j + 1)

            # For deleting a character
            delete = float("inf")
            if i < n:
                delete = dp(i + 1, j)

            equal = float("inf")
            replace = float("inf")
            if i < n and j < m:
                # First try to pass if they're equal
                if word1[i] == word2[j]:
                    equal = dp(i + 1, j + 1)
                else:
                    # For replacing a character
                    replace = dp(i + 1, j + 1)

            return min(equal, 1 + min(insert, delete, replace))

        return dp(0, 0)

    def minDistanceTabulation(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        table = [[float("inf")] * (m + 1) for _ in range(n + 1)]
        table[0][0] = 0

        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0:
                    table[i][j] = min(table[i][j], 1 + table[i - 1][j])

                if j > 0:
                    table[i][j] = min(table[i][j], 1 + table[i][j - 1])

                if i > 0 and j > 0:
                    if word1[i - 1] == word2[j - 1]:
                        table[i][j] = min(table[i][j], table[i - 1][j - 1])
                    else:
                        table[i][j] = min(table[i][j], 1 + table[i - 1][j - 1])
        print(table)
        return table[n][m]
