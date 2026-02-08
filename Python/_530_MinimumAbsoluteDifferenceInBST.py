from typing import Optional
import unittest
import time


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """Given the `root` of a Binary Search Tree (BST), return *the minimum
        absolute difference between the values of any two different nodes in the
        tree*.

        Args:
            root (Optional[TreeNode]): root of a Binary Search Tree

        Returns:
            int: the minimum absolute difference between the values of any two
            different nodes in the tree
        """
        prev = None  # the value of the previous node
        diff = float("inf")

        def traverse(node):
            """Since BST is an ordered tree, the minimum difference will always 
            be the difference between a node and the one right before it.

            Args:
                node (_type_): the current node
            """
            nonlocal prev, diff

            if not node:
                return

            # Farthest left has the lowest value
            traverse(node.left)

            # If the current nodes isn't thel lowest value, then compare the
            # difference between this node and the previous node, to the current
            # difference and take the smaller.
            if prev is not None:
                diff = min(diff, node.val - prev)

            # Set the previous value to this node before moving on.
            prev = node.val

            traverse(node.right)

        # Traverse the tree in order recursively. Find the difference between
        # each node and the previous node. Return the smallest difference.
        traverse(root)
        
        return int(diff)


class TestSolution(unittest.TestCase):

    total_time = 0
    count = 0

    def setUp(self) -> None:
        self.sol = Solution()
        self.start = time.perf_counter()
        TestSolution.count += 1

    def tearDown(self) -> None:
        end = time.perf_counter()
        runtime = end - self.start
        TestSolution.total_time += runtime
        runtime = f"{runtime * 1000:.0f}"
        print(f"Test {TestSolution.count}: {runtime} ms")

    @classmethod
    def tearDownClass(cls):
        runtime = f"{(TestSolution.total_time / TestSolution.count) * 1000:.0f}"
        print(f"Average runtime: {runtime} ms")

    def test_example1(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_example2(self):
        root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
        self.assertEqual(self.sol.getMinimumDifference(root), 1)

    def test_two_nodes_with_0(self):
        root = TreeNode(100_000, TreeNode(0))
        self.assertEqual(self.sol.getMinimumDifference(root), 100_000)


if __name__ == "__main__":
    unittest.main()
