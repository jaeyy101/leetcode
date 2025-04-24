class Solution:
    def __init__(self):
        pass

    def computeLPS(self, needle: str):
        m = len(needle)
        lps = [0 for _ in range(m)]

        needle_len = 0
        i = 1

        while i < m:
            if needle[i] == needle[needle_len]:
                needle_len += 1
                lps[i] = needle_len
                i += 1
            else:
                if needle_len != 0:
                    needle_len = lps[needle_len - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def strStr(self, haystack: str, needle: str):
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        if n < m:
            return -1

        lps = self.computeLPS(needle)

        i = 0
        j = 0

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == m:
                return i - j
            elif i < n and haystack[i] != needle[j]:
                if j == 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1


solution = Solution()
print(solution.strStr("ababcabcabababd", "ababd"))
