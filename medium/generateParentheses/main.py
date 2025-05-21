class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []

        def backtrack(opening, closing):
            if opening == closing == n:
                res.append("".join(path))
                return

            if opening < n:
                path.append("(")
                backtrack(opening + 1, closing)
                path.pop()

            if closing < opening:
                path.append(")")
                backtrack(opening, closing + 1)
                path.pop()

        backtrack(0, 0)
        return res
