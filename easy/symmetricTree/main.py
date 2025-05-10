from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.checkSymmetry(root.left, root.right)

    def checkSymmetry(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (
            left.val == right.val
            and self.checkSymmetry(left.left, right.right)
            and self.checkSymmetry(left.right, right.left)
        )

    def isSymmetricIterative(self, root: TreeNode):
        if not root:
            return True

        queue = deque([(root.left, root.right)])
        while queue:
            for _ in range(len(queue)):
                p, q = queue.popleft()
                if not p and not q:
                    continue
                elif not p or not q:
                    return False

                if p.val != q.val:
                    return False

                queue.append((p.left, q.right))
                queue.append((p.right, q.left))
        return True


s = TreeNode(1)
s.left = TreeNode(2)
s.right = TreeNode(2)
s.left.left = TreeNode(3)
s.left.right = TreeNode(4)
s.right.left = TreeNode(4)
s.right.right = TreeNode(3)

print(Solution().isSymmetricIterative(s))
