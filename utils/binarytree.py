class TreeNode:
    def __init__(self, value=None):
        self.val = value
        self.left: TreeNode = None
        self.right: TreeNode = None


class BinaryTree:
    def __init__(self):
        self.head = None
