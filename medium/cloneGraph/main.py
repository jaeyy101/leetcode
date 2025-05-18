# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: "list[Node] | None" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        old_to_new_map: dict[Node, Node] = {}

        def dfs_clone(current: Node) -> Node:
            if current in old_to_new_map:
                return old_to_new_map[current]

            clone = Node(current.val)
            old_to_new_map[current] = clone

            for neighbor in current.neighbors:
                clone.neighbors.append(dfs_clone(neighbor))
            return clone

        return dfs_clone(node)
