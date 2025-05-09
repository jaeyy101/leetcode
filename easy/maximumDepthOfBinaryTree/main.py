class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_branch = self.maxDepth(root.left) + 1
        right_branch = self.maxDepth(root.right) + 1

        return min(left_branch, right_branch)

    def maxDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth


# head = TreeNode(3)
# head.left = TreeNode(9)
# head.right = TreeNode(20)
# head.right.left = TreeNode(15)
# head.right.right = TreeNode(7)
# head.right.right.left = TreeNode(9)

# print(Solution().maxDepth1(head))
