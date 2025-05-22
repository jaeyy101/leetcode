from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(
        self,
        val,
        isLeaf,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def helper(x, y, size):
            if all_same(grid, x, y, size):
                return Node(val=grid[x][y] == 1, isLeaf=True)
            else:
                half = size // 2
                return Node(
                    val=True,
                    isLeaf=False,
                    topLeft=helper(x, y, half),
                    topRight=helper(x, y + half, half),
                    bottomLeft=helper(x + half, y, half),
                    bottomRight=helper(x + half, y + half, half),
                )

        def all_same(grid, x, y, size):
            first_val = grid[x][y]
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != first_val:
                        return False
            return True

        return helper(0, 0, len(grid))


s = Solution().construct([[0, 1], [1, 0]])


def print_quadtree(node: Node):
    if not node:
        return

    print(node.val)
    print_quadtree(node.topLeft)
    print_quadtree(node.topRight)
    print_quadtree(node.bottomLeft)
    print_quadtree(node.bottomRight)


print_quadtree(s)
