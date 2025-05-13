# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_height = self.get_height(root, True)
        right_height = self.get_height(root, False)

        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_height(self, node: TreeNode, left):
        h = 0
        while node:
            h += 1
            node = node.left if left else node.right
        return h
