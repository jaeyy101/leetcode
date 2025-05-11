# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        if not root:
            return 0
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)
