class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        word_length = 0

        for i in range(n - 1, -1, -1):
            if s[i] == " " and word_length > 0:
                break

            if s[i].isalpha():
                word_length += 1

        return word_length


s = Solution()
print(s.lengthOfLastWord("sk"))
