class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        
        # if len(nums) == 1:
        #     return 1
        
        # k = 1
        # l = 1
        # slow = 0
        # fast = 1
        # current_pairs = 0

        # while slow < len(nums) and fast < len(nums):

        #     if nums[slow] == nums[fast]:

        #         if current_pairs < 1:
        #             l += 1
        #             current_pairs += 1
        #         else:
        #             fast += 1

        #     else:
        #         nums[l] = nums[fast]
        #         k += 1
        #         l += 1
        #         slow = fast
        #         current_pairs = 0
        #         fast += 1

        # print(nums)
        # return k

        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1

        print(nums)
        return i
    

s = Solution()
s.removeDuplicates([1,1,1,1,2,2])