class TreeNode:
    def __init__(self, value=None):
        self.val = value
        self.left: TreeNode = None
        self.right: TreeNode = None


class BinaryTree:
    def __init__(self):
        self.head = None


def postorder(root: TreeNode):
    if not root:
        return

    print(root.val)
    postorder(root.left)
    postorder(root.right)


s = TreeNode(3)
s.left = TreeNode(9)
s.left.left = TreeNode(10)
s.right = TreeNode(20)
s.right.left = TreeNode(15)
s.right.right = TreeNode(7)
# s.right.left.right = TreeNode(8)

postorder(s)
