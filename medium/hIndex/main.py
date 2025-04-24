class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        bucket = [0] * (n+1)

        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        print(bucket)
        count = 0
        for h in range(n, -1, -1):
            count += bucket[h]
            if count >= h:
                return h

        return 0

s = Solution()
ans = s.hIndex([0,1,2,3,4])
print(ans)
