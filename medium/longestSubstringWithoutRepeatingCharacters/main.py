class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        n = len(s)

        longest = 0
        unique = set()
        left = 0
        for right in range(n):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            longest = max(longest, right - left + 1)
        return longest

    def lengthOfLongestSubstring2(self, s: str) -> int:
        freq = [0] * 128

        left = 0
        n = len(s)
        longest = 0
        for right in range(n):
            right_index = ord(s[right])
            while freq[right_index] > 0:
                freq[ord(s[left])] -= 1
                left += 1
            freq[right_index] += 1
            longest = max(longest, right - left + 1)

        return longest


print(Solution().lengthOfLongestSubstring2(" "))
