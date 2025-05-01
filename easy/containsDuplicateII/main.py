class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_map = {}
        for i, num in enumerate(nums):
            if num in num_map:
                if i - num_map[num] <= k:
                    return True
            num_map[num] = i
        return False
