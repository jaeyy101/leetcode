class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        n = len(words)
        output = []

        i = 0
        while i < n:
            total = 0
            count = 0
            line = []

            while i < n:
                if total + len(words[i]) + count <= maxWidth:
                    total += len(words[i])
                    line.append(words[i])
                    count += 1
                    i += 1
                else:
                    break

            if i == n:
                final = " ".join(line)
                output.append(final + " " * (maxWidth - total - count + 1))
            else:
                output.append(self.formString(line, total, count, maxWidth))

        return output

    def formString(self, words: list[str], total: int, count: int, maxWidth: int):
        remaining = maxWidth - total
        if count == 1:
            return words[0] + " " * remaining

        base = remaining // (count - 1)
        remainder = remaining % (count - 1)
        spaces = [base] * (count - 1)
        for i in range(remainder):
            spaces[i] += 1

        output = ""
        for i in range(count):
            output += words[i]
            if i != count - 1:
                output += " " * spaces[i]

        return output


s = Solution()
print(
    s.fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
)
