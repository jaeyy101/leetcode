class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        words = s.split(" ")
        if n != len(words):
            return False

        bijection = {}
        used_letters = set()

        for i in range(n):
            if words[i] not in bijection:
                if pattern[i] in used_letters:
                    return False

                bijection[words[i]] = pattern[i]
                used_letters.add(pattern[i])
            elif bijection[words[i]] != pattern[i]:
                return False

        return True


print(Solution().wordPattern("abba", "dog cat cat dog"))
