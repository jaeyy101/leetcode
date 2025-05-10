from collections import deque


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        queue = deque([root])
        while queue:
            dummy = Node(0)
            curr = dummy
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                curr.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curr = curr.next

        return root
