class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                last = stack.pop() if stack else "#"
                if last != char:
                    return False

        return not stack


print(Solution().isValid("(()"))
