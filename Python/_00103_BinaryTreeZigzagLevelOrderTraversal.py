from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Given the `root` of a binary tree, return *the zigzag level order
        traversal of its nodes' values*. (i.e., from left to right, then right
        to left for the next level and alternate between).

        Args:
            root (Optional[TreeNode]): the root of a binary tree

        Returns:
            List[List[int]]: the zigzag level order traversal of node values
        """

        if not root:
            return []

        res = []
        queue = deque([root])
        level = 0 # current level of the tree traversal

        while queue:
            vals = []
            # For each node at this level...
            for _ in range(len(queue)):
                # Pop the node from the queue and add its value to the list.
                node = queue.popleft()
                vals.append(node.val)

                # Add the next level nodes to the queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # If this is an even level, add the values in left to right order.
            # If this is an odd level, add the values in right to left order.
            res.append(vals if level % 2 == 0 else vals[::-1])

            level += 1

        return res


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected = [[3], [20, 9], [15, 7]]
        actual = self.sol.zigzagLevelOrder(root)
        self.assertEqual(expected, actual)

    def test_example2(self):
        root = TreeNode(1)
        expected = [[1]]
        actual = self.sol.zigzagLevelOrder(root)
        self.assertEqual(expected, actual)

    def test_example3(self):
        root = None
        expected = []
        actual = self.sol.zigzagLevelOrder(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
