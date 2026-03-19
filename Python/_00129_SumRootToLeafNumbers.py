from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """You are given the `root` of a binary tree containing digits from `0` 
        to `9` only.

        Each root-to-leaf path in the tree represents a number.

        - For example, the root-to-leaf path `1 -> 2 -> 3` represents the number 
        `123`.
        Return *the total sum of all root-to-leaf numbers*. Test cases are 
        generated so that the answer will fit in a **32-bit** integer.

        A **leaf** node is a node with no children.

        Args:
            root (Optional[TreeNode]): the root of a binary tree

        Returns:
            int: the total sum of all root-to-leaf numbers
        """

        if not root:
            return 0

        def get_sum(node, running_sum, total):
            """Calculate the sum of all root-to-leaf "numbers".

            Args:
                node (TreeNode): the current node
                running_sum (int): a running sum for each path
                total (int): the total sum

            Returns:
                int: the total sum
            """

            # Each time we get to a leaf, add the running sum to the total
            if not node.left and not node.right:
                return total + running_sum * 10 + node.val

            # Start with the most significant digit, and add each digit in the
            # path to the leaf.
            running_sum = running_sum * 10 + node.val

            if node.left:
                total = get_sum(node.left, running_sum, total)
            if node.right:
                total = get_sum(node.right, running_sum, total)

            return total

        return get_sum(root, 0, 0)


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        expected = 25
        actual = self.sol.sumNumbers(root)
        self.assertEqual(expected, actual)

    def test_example2(self):
        root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
        expected = 1026
        actual = self.sol.sumNumbers(root)
        self.assertEqual(expected, actual)

    def test_example_one_node(self):
        root = TreeNode(5)
        expected = 5
        actual = self.sol.sumNumbers(root)
        self.assertEqual(expected, actual)

    def test_example_no_right(self):
        root = TreeNode(5, TreeNode(3))
        expected = 53
        actual = self.sol.sumNumbers(root)
        self.assertEqual(expected, actual)

    def test_example_no_left(self):
        root = TreeNode(5, None, TreeNode(3))
        expected = 53
        actual = self.sol.sumNumbers(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
