class Solution:
    def reverseWords(self, s: str) -> str:
        # Cheating
        # words = s.split(" ")

        # filtered_words = [word for word in reversed(words) if word != ""]

        # return " ".join(filtered_words)

        # My solution. It's ass fr
        n = len(s)
        slow, fast = n - 1, n - 1
        steps = 0

        result = ""
        while slow >= 0:
            if s[fast] == " " and s[slow] == " ":
                fast -= 1
                slow -= 1
            elif (fast < 0 and s[fast] != " ") or (s[fast] == " " and s[slow] != " "):
                slow = fast + 1
                while steps > 0:
                    result += s[slow]
                    steps -= 1
                    slow += 1

                result += " "
                fast -= 1
                slow = fast
            else:
                while s[fast] != " ":
                    fast -= 1
                    steps += 1
                    if fast < 0:
                        break

        return result.strip()
