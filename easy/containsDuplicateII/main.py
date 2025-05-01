class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        num_set = set()
        for i in range(k + 1):
            if nums[i] in num_set:
                return True
            num_set.add(nums[i])

        right = k + 1
        while right < n:
            num_set.remove(nums[right - k - 1])
            if nums[right] in num_set:
                return True
            num_set.add(nums[right])
            right += 1

        return True
