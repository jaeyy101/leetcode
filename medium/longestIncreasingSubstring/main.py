import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = []

        for num in nums:
            # Find the insertion point in tails
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                tails.append(num)  # New longer subsequence
            else:
                tails[idx] = num  # Replace to keep smallest possible tail

        return len(tails)


Solution().lengthOfLIS([0, 1, 0, 3, 2, 3])
