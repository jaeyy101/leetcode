class Solution:
    def calculate(self, s: str) -> int:
        return self.calcRecursively(s, 0)

    def calcRecursively(self, s: str, index: int) -> tuple[int, int]:
        stack = []

        while index < len(s):
            if s[index] == ")":
                return stack[0], index + 1

            if s[index] == " ":
                index += 1
                continue

            if s[index] == "(":
                # Make recursive call when opening parenthesis encountered
                # to get result of evaluated expression and new index
                num, new_index = self.calcRecursively(s, index + 1)
                index = new_index

                if len(stack) > 1:
                    operation = stack.pop()
                    first = stack.pop()
                    res = first + num if operation == "+" else first - num
                    stack.append(res)
                else:
                    if stack:
                        stack.pop()
                        num = -num
                    stack.append(num)
            elif s[index].isdigit():
                digits = []
                while index < len(s) and s[index].isdigit():
                    digits.append(s[index])
                    index += 1
                num = int("".join(digits))

                # If there are numbers already in stack
                if len(stack) > 1:
                    operation = stack.pop()
                    first = stack.pop()
                    res = first + num if operation == "+" else first - num
                    stack.append(res)
                else:  # The first number to come around
                    if stack:
                        stack.pop()
                        num = -num
                    stack.append(num)
            else:  # Current character is an operation
                stack.append(s[index])
                index += 1

        return stack[0]


print(Solution().calculate("-2+  (-4-2)"))
