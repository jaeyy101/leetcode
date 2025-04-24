class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        required_to_brige_gap = 1

        for i in range(n-1, -1, -1):
            if nums[i] == 0 or nums[i] < required_to_brige_gap:
                required_to_brige_gap += 1
            else:
                required_to_brige_gap = 1

        return required_to_brige_gap == 1
    

s = Solution()
print(s.canJump([4,0,0,0,0]))