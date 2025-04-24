class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)

        i = 0
        j = 0

        while i < n and j < m:
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == m


s = Solution()
print(s.isSubsequence("axc", "ahbgdc"))
