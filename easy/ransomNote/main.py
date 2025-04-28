class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0] * 26
        ORD_A = ord("a")

        for letter in magazine:
            freq[ord(letter) - ORD_A] += 1

        for letter in ransomNote:
            index = ord(letter) - ORD_A
            if freq[index] == 0:
                return False
            freq[index] -= 1

        return True


print(Solution().canConstruct("ac", "ab"))
