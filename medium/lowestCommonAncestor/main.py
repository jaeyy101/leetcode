# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ancestor = None

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right

    def lowestCommonAncestor1(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def helper(node):
            if not node or self.ancestor:
                return False

            in_left = helper(node.left)
            in_right = helper(node.right)

            if in_left and in_right:
                self.ancestor = node
            elif node in [p, q] and (in_left or in_right):
                self.ancestor = node
            else:
                return node in [p, q] or in_left or in_right
            return False

        helper(root)
        return self.ancestor
