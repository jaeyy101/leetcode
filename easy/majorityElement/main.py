class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m = None
        c = 0

        for num in nums:
            if c == 0:
                m = num
                c = 1
            elif m == num:
                c += 1
            else:
                c -= 1
        
        return m
    

s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))