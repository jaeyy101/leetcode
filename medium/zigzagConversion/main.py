class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s

        res = []
        toogle = False

        for i in range(numRows):
            index = i
            toogle = i > numRows - i - 1

            while index < n:
                res.append(s[index])
                if i == 0 or i == numRows - 1:
                    next_push = 2 * (numRows - 1)
                else:
                    low = 2 * min(i, numRows - i - 1)
                    high = 2 * max(i, numRows - i - 1)

                    next_push = low if toogle else high
                    toogle = not toogle
                index += next_push

        return "".join(res)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
