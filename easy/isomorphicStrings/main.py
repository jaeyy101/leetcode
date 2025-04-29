class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in used:
                    return False
                map[s[i]] = t[i]
                used.add(t[i])
            elif map[s[i]] != t[i]:
                return False
        return True


print(Solution().isIsomorphic("badc", "baba"))
