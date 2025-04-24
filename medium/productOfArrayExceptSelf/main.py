class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Naive
        # result = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             result[i] *= nums[j]

        # return result

        n = len(nums)
        result = [1] * n

        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result
    
s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))