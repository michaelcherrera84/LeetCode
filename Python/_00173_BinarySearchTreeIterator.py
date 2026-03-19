from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        """Initializes an object of the `BSTIterator` class.

        Args:
            root (Optional[TreeNode]): the root of a binary search tree
        """

        self.queue = deque()  # queue of all values

        def build_queue(node):
            if not node:
                return

            build_queue(node.left)
            self.queue.append(node.val)
            build_queue(node.right)

        build_queue(root)

    def next(self) -> int:
        """Return the next value in the tree.

        Returns:
            int: the next value in the tree
        """
        return self.queue.popleft()

    def hasNext(self) -> bool:
        """Return `True` if there are values left in the tree, or `False`
        otherwise.

        Returns:
            bool: `True` if there are values left in the tree, or `False`
            otherwise
        """
        return len(self.queue) > 0


import unittest


class Test_Solution(unittest.TestCase):
    def test_example1(self):
        root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
        bSTIterator = BSTIterator(root)
        self.assertEqual(3, bSTIterator.next())
        self.assertEqual(7, bSTIterator.next())
        self.assertTrue(bSTIterator.hasNext())
        self.assertEqual(9, bSTIterator.next())
        self.assertTrue(bSTIterator.hasNext())
        self.assertEqual(15, bSTIterator.next())
        self.assertTrue(bSTIterator.hasNext())
        self.assertEqual(20, bSTIterator.next())
        self.assertFalse(bSTIterator.hasNext())


if __name__ == "__main__":
    unittest.main()
