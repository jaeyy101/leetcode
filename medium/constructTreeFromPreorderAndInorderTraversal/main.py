class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_index = [0]

        def helper(left, right):
            if left > right:
                return None

            val = preorder[pre_index[0]]
            pre_index[0] += 1
            root = TreeNode(val)
            index_at_inorder = inorder_map[val]

            root.left = helper(left, index_at_inorder - 1)
            root.right = helper(index_at_inorder + 1, right)

            return root

        return helper(0, len(inorder) - 1)
