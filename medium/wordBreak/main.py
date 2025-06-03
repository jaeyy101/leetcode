class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        from functools import lru_cache

        word_set = set(wordDict)
        max_len = max(map(len, wordDict)) if wordDict else 0

        @lru_cache(maxsize=None)
        def dp(i):
            if i == len(s):
                return True
            for j in range(i + 1, min(len(s) + 1, i + max_len + 1)):
                word = s[i:j]
                if word in word_set and dp(j):
                    return True
            return False

        return dp(0)


print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
