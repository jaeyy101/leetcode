# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        post_index = [len(inorder) - 1]

        def helper(left, right):
            if left > right:
                return None
            val = postorder[post_index[0]]
            post_index[0] -= 1
            index_at_inorder = inorder_map[val]
            root = TreeNode(val)

            root.right = helper(index_at_inorder + 1, right)
            root.left = helper(left, index_at_inorder - 1)

            return root

        return helper(0, len(inorder) - 1)


s = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])


def print_tree(s):
    if not s:
        return
    print_tree(s.left)
    print_tree(s.right)
    print(s.val)


print_tree(s)
