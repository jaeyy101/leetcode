class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        position = 0
        temp = [*nums1]

        while i < m and j < n:
            if temp[i] < nums2[j]:
                nums1[position] = temp[i]
                i += 1
                position += 1
            else:
                nums1[position] = nums2[j]
                j += 1
                position += 1

        while i < m:
            nums1[position] = temp[i]
            i += 1
            position += 1

        while j < n:
            nums1[position] = nums2[j]
            j += 1
            position += 1

        print(nums1)