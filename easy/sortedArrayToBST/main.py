# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divideAndConquer(left, right) -> Optional[TreeNode]:
            if not left < right:
                return None

            mid = (left + right) // 2

            node = TreeNode(nums[mid])
            node.left = divideAndConquer(left, mid)
            node.right = divideAndConquer(mid + 1, right)
            return node

        return divideAndConquer(0, len(nums))
