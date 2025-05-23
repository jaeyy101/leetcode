class Solution:
    def peakElement(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            bigger_than_latter = nums[mid] > nums[mid + 1]
            bigger_than_former = nums[mid] > nums[mid - 1]

            if bigger_than_former and bigger_than_latter:
                return mid

            if bigger_than_former:
                left = mid + 1
            else:
                right = mid - 1

        return left


print(Solution().peakElement([1, 2, 1, 3, 5, 6, 8]))
