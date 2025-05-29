class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            lsb = n & 1
            res = (res << 1) | lsb
            n >>= 1
        return res


print(Solution().reverseBits(4294967295))
