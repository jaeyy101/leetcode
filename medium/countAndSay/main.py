# Only had time to implement the naive algorithm. TYPE SHIT. SLATT
class Solution:
    def countAndSay(self, n: int) -> str:
        base = "1"

        for _ in range(1, n + 1):
            base = self.say(base)

        return base

    def say(self, str):
        i = 0
        n = len(str)
        result = ""
        while i < n:
            count = 1
            current = str[i]
            i += 1
            while i < n and str[i] == current:
                count += 1
                i += 1
            result += f"{count}{current}"

        return result


a = 2
print(Solution().countAndSay(a))
