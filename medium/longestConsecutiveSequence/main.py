class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_map = {}
        for num in nums:
            nums_map[num] = 1

        longest = 0
        for key in nums_map:
            count = 0
            curr = key
            while curr in nums_map:
                if nums_map[curr] != 1:
                    count += nums_map[curr]
                    break
                nums_map[curr] = count + 1
                count += 1
                curr += 1
            longest = max(longest, count)
            nums_map[key] = count

        return longest

    def longestConsecutiveII(self, nums: list[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                curr = num + 1
                while curr + 1 in nums:
                    curr += 1
                longest = max(longest, curr - num + 1)

        return longest


print(Solution().longestConsecutiveII([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
