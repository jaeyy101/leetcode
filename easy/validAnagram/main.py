class Solution:
    def validAnagram(self, s, t):
        return self.counter(s) == self.counter(t)

    def counter(self, s):
        total = 0
        i = 0
        length = len(s)
        while i < length:
            total += hash(s[i])
            i += 1

        return total


def main():
    s = input("Enter first word: ")
    t = input("Enter second word: ")

    sol = Solution()
    if sol.validAnagram(s, t):
        print(f"{t} is an anagram of {s}")
    else:
        print(f"{t} is not an anagram of {s}")


if __name__ == "__main__":
    main()
