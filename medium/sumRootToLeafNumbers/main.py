# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbersQueue(self, root: TreeNode) -> int:
        queue = deque([(root, root.val)])

        ans = 0
        while queue:
            for _ in range(len(queue)):
                node, num = queue.popleft()
                if not node.left and not node.right:
                    ans += num

                if node.left:
                    left_num = num * 10 + node.left.val
                    queue.append((node.left, left_num))
                if node.right:
                    right_num = num * 10 + node.right.val
                    queue.append((node.right, right_num))
        return ans

    def sumNumbersStack(self, root: TreeNode) -> int:
        stack = [(root, root.val)]

        ans = 0
        while stack:
            node, curr_num = stack.pop()
            if not node.left and not node.right:
                ans += curr_num

            if node.right:
                right_num = curr_num * 10 + node.right.val
                stack.append((node.right, right_num))

            if node.left:
                left_num = curr_num * 10 + node.left.val
                stack.append((node.left, left_num))

        return ans

    def sumNumbersRec(self, root: TreeNode) -> int:
        ans = [0]

        def helper(node: TreeNode, curr_num: int):
            if not node.left and not node.right:
                ans[0] += curr_num

            if node.left:
                helper(node.left, curr_num * 10 + node.left.val)
            if node.right:
                helper(node.right, curr_num * 10 + node.right.val)

        helper(root, root.val)
        return ans[0]
