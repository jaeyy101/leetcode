# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self._prev = None
        self._ans = float("inf")

        def helper(node):
            if node:
                helper(node.left)
                if self._prev is not None:
                    self._ans = min(self._ans, node.val - self._prev)
                self._prev = node.val
                helper(node.right)

        helper(root)
        return self._ans
