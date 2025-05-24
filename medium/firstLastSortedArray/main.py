class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = [-1, -1]

        left = 0
        right = n

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if 0 <= left < n and nums[left] == target:
            ans[0] = left

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        if 0 <= right < n and nums[right] == target:
            ans[1] = right
        return ans
