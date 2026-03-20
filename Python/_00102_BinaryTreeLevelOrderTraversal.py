from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Given the `root` of a binary tree, return *the level order traversal
        of its nodes' values*. (i.e., from left to right, level by level).

        Args:
            root (Optional[TreeNode]): the root of a binary tree

        Returns:
            List[List[int]]: level order traversal of node values
        """
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            n = len(queue) # number of nodes at this level
            nodes = [] # node values at this level

            # For each node at this level...
            for i in range(n):
                # Get the node from the queue (FIFO)
                node = queue.popleft()
                # Add the node's value to the list.
                nodes.append(node.val)

                # Add the next level children to the queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add this level's values to the result list.
            res.append(nodes)

        return res


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected = [[3], [9, 20], [15, 7]]
        actual = self.sol.levelOrder(root)
        self.assertEqual(expected, actual)

    def test_example2(self):
        root = TreeNode(1)
        expected = [[1]]
        actual = self.sol.levelOrder(root)
        self.assertEqual(expected, actual)

    def test_example3(self):
        root = None
        expected = []
        actual = self.sol.levelOrder(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
