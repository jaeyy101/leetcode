class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            new_min = val
        else:
            last = self.stack[-1]
            new_min = min(val, last[1])
        self.stack.append([val, new_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        last = self.stack[-1]
        return last[1]
