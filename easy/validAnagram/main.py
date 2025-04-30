class Solution:
    def isAnagramNaive(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        for i in range(n):
            if s[i] != t[i]:
                return False

        return True

    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False

        # s_counts = {}
        # for letter in s:
        #     s_counts[letter] = s_counts.get(letter, 0) + 1
        ord_a = ord("a")
        s_counts = [0] * 26
        for letter in s:
            s_counts[ord(letter) - ord_a] += 1

        for i in range(n):
            index = ord(t[i]) - ord_a
            if not s_counts[index] > 0:
                return False

            s_counts[index] -= 1

        return True


print(Solution().isAnagram("anagram", "nagaram"))
