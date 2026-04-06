# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


from typing import List


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        """
        Given a `n * n` matrix `grid` of `0's` and `1's` only. We want to
        represent `grid` with a Quad-Tree.

        Return *the root of the Quad-Tree representing* `grid`.

        A Quad-Tree is a tree data structure in which each internal node has
        exactly four children. Besides, each node has two attributes:
        - `val`: True if the node represents a grid of 1's or False if the node
        represents a grid of 0's. Notice that you can assign the `val` to True
        or False when `isLeaf` is False, and both are accepted in the answer.
        - `isLeaf`: True if the node is a leaf node on the tree or False if the
        node has four children.
        ```
        class Node {
            public boolean val;
            public boolean isLeaf;
            public Node topLeft;
            public Node topRight;
            public Node bottomLeft;
            public Node bottomRight;
        }
        ```
        We can construct a Quad-Tree from a two-dimensional area using the
        following steps:
        1. If the current grid has the same value (i.e all `1's` or all `0's`)
        set `isLeaf` True and set `val` to the value of the grid and set the
        four children to Null and stop.
        2. If the current grid has different values, set `isLeaf` to False and
        set `val` to any value and divide the current grid into four sub-grids
        as shown in the photo.
        3. Recurse for each of the children with the proper sub-grid.


        Args:
            grid (List[List[int]]): the grid from which to construct the tree

        Returns:
            Node: the root of the tree
        """

        def is_one_node(i, j, length):
            """
            Determine if a grid is one node by checking if all values are
            the same.

            Args:
                i (int): first row of grid
                j (int): first column of grid
                length (int): height and width of a grid

            Returns:
                bool: `True` if this grid represents a `Node` or `False` otherwise
            """

            for r in range(i, i + length):
                for c in range(j, j + length):
                    if grid[r][c] != grid[i][j]:
                        return False
            return True

        def build_tree(i, j, length):
            """
            Build the tree by recursively scanning the grid searching for
            sub-grids

            Args:
                i (int): first row of the current grid
                j (int): first column of the current grid
                length (int): height and width of the current grid

            Returns:
                Node: a node of the tree
            """
            if is_one_node(i, j, length):
                return Node(grid[i][j], 1, None, None, None, None)

            node = Node(
                1,
                0,
                build_tree(i, j, length // 2),
                build_tree(i, j + length // 2, length // 2),
                build_tree(i + length // 2, j, length // 2),
                build_tree(i + length // 2, j + length // 2, length // 2),
            )

            return node

        return build_tree(0, 0, len(grid))


from collections import deque
import unittest


class TestSolution(unittest.TestCase):
    """
    The output represents the serialized format of a Quad-Tree using level order
    traversal, where `null` signifies a path terminator where no node exists
    below.

    It is very similar to the serialization of the binary tree. The only
    difference is that the node is represented as a list `[isLeaf, val]`.

    If the value of `isLeaf` or `val` is True we represent it as 1 in the list
    `[isLeaf, val]` and if the value of isLeaf or val is False we represent it
    as `0`.
    """

    def setUp(self) -> None:
        self.sol = Solution()

    def to_list(self, node: Node):
        res = []
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            if curr:
                res.append([curr.isLeaf, curr.val])

                queue.append(curr.topLeft)
                queue.append(curr.topRight)
                queue.append(curr.bottomLeft)
                queue.append(curr.bottomRight)
            else:
                res.append(None)

        for i in range(len(res) - 1, -1, -1):
            if res[i] is not None:
                res = res[: i + 1]
                break

        return res

    def test_example1(self):
        grid = [[0, 1], [1, 0]]
        output = self.sol.construct(grid)
        expected = [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
        actual = self.to_list(output)
        self.assertEqual(expected, actual)

    def test_example2(self):
        grid = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
        ]
        output = self.sol.construct(grid)
        expected = [
            [0, 1],
            [1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            None,
            None,
            None,
            None,
            [1, 0],
            [1, 0],
            [1, 1],
            [1, 1],
        ]
        actual = self.to_list(output)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
