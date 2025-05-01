class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        while True:
            if n == 1:
                return True
            num_set.add(n)

            new_n = 0
            while n > 0:
                digit = n % 10
                new_n += digit**2
                n = n // 10

            if new_n in num_set:
                return False
            n = new_n


print(Solution().isHappy(160))
