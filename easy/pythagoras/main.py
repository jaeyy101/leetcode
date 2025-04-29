import math


class Solution:
    def pythagoras(self, n: int) -> int:
        res = 0
        limit = n**2

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                sum_squares = i**2 + j**2

                if sum_squares > limit:
                    break

                bigger_num = sum_squares**0.5
                if bigger_num % 1 == 0:
                    print(i, j, int(bigger_num))
                    res += 2

        return res


print(Solution().pythagoras(20))
