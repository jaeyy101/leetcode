class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        conversions = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        i = 0
        while i < n:
            current = conversions[s[i]]

            if i + 1 < n and current < conversions[s[i + 1]]:
                result += conversions[s[i + 1]] - current
                i += 2
            else:
                result += current
                i += 1

        return result


s = Solution()
print(s.romanToInt("MCMXCIV"))
