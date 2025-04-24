class Solution:
    def maxArea(self, height: list[int]) -> int:
        start = 0
        end = len(height) - 1

        max_area = 0
        while start < end:
            distance = end - start
            left = height[start]
            right = height[end]

            new_area = distance * min(left, right)
            max_area = max(max_area, new_area)

            if left < right:
                start += 1
            else:
                end -= 1

        return max_area


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 1, 7]))
