class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        if m < n:
            a, b = b, a
            m, n = n, m

        carry_over = 0
        res = []

        i = 0
        while i < n:
            a_digit = int(a[m - i - 1])
            b_digit = int(b[n - i - 1])
            total = a_digit + b_digit + carry_over
            res.append(str(total % 2))
            carry_over = total // 2
            i += 1

        while i < m:
            digit = int(a[m - i - 1])
            total = digit + carry_over
            res.append(str(total % 2))
            carry_over = total // 2
            i += 1

        if carry_over == 1:
            res.append(str(carry_over))

        return "".join(reversed(res))
