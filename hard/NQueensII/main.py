class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [False] * n
        main_diag = set()
        alt_diag = set()

        def backtrack(row):
            if row == n:
                return 1

            res = 0
            for col in range(n):
                if cols[col]:
                    continue
                if row - col in main_diag or row + col in alt_diag:
                    continue

                cols[col] = True
                main_diag.add(row - col)
                alt_diag.add(row + col)

                res += backtrack(row + 1)

                cols[col] = False
                main_diag.remove(row - col)
                alt_diag.remove(row + col)
            return res

        return backtrack(0)
