class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if not token[-1].isdigit():
                second = stack.pop()
                first = stack.pop()
                match token:
                    case "+":
                        val = first + second
                    case "-":
                        val = first - second
                    case "*":
                        val = first * second
                    case "/":
                        val = int(first / second)
                stack.append(val)
            else:
                stack.append(int(token))

        return stack[0]


print(
    Solution().evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)
