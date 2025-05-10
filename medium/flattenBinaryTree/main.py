class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node: TreeNode):
            if not node:
                return None, None

            left_head, left_tail = helper(node.left)
            right_head, right_tail = helper(node.right)
            last = None

            if left_head:
                node.right = left_head
                left_tail.right = right_head
            else:
                node.right = right_head

            last = right_tail or left_tail or node

            node.left = None
            return node, last

        helper(root)

    def flattenStack(self, root: TreeNode) -> None:
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            if stack:
                node.right = stack[-1]

            node.left = None
