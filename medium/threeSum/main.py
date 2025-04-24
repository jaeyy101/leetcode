class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Not my best work, but whatever
        nums.sort()
        n = len(nums)

        result = []
        i = 0
        while i < n:
            number = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                if left == i:
                    left += 1
                    continue

                if right == i:
                    right -= 1
                    continue

                total = nums[left] + nums[right] + number
                if total == 0:
                    result.append([number, nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif total > 0:
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1

            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return result


print(Solution().threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]))
