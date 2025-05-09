class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        new_left = self.invertTree(root.right)
        new_right = self.invertTree(root.left)
        root.left = new_left
        root.right = new_right

        return root

    def invertTreeQueue(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                temp_left = node.left
                node.left = node.right
                node.right = temp_left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
