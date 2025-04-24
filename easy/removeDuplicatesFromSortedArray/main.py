class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        previous = float("-inf")

        for i in range(len(nums)):
            if previous < nums[i]:
                nums[k] = nums[i]
                k += 1
                previous = nums[i]
            
        return k

