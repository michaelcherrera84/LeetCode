from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Given the `root` of a binary tree, flatten the tree into a "linked
        list":

        - The "linked list" should use the same `TreeNode` class where the
        `right` child pointer points to the next node in the list and the `left`
        child pointer is always `null`.
        - The "linked list" should be in the same order as a pre-order traversal
        of the binary tree.

        Args:
            root (Optional[TreeNode]): the root of a binary tree
        """

        if not root:
            return
        
        curr = root

        while curr:
            # If the current node has a left node, find the right most node of
            # the left subtre,e and connect it to the node right of the current.
            # Then swap the left subtree to the right side and clear the left.
            if curr.left:
                temp = curr.left

                while temp.right:
                    temp = temp.right

                temp.right = curr.right
                curr.right = curr.left
                curr.left = None

            # Advance to the next node.
            curr = curr.right

import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def compare(self, l1, l2):
        if not l1 and not l2:
            return True
        if l1 and not l2 or l2 and not l1:
            return False
        if l1.val != l2.val:
            return False
        return self.compare(l1.left, l2.left) and self.compare(l1.right, l2.right)

    def test_example1(self):
        root = TreeNode(
            1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))
        )
        expected = TreeNode(
            1,
            None,
            TreeNode(
                2,
                None,
                TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))),
            ),
        )
        self.sol.flatten(root)
        self.assertTrue(self.compare(expected, root))

    def test_example2(self):
        root = None
        expected = None
        self.sol.flatten(root)
        self.assertTrue(self.compare(expected, root))

    def test_example3(self):
        root = TreeNode(0)
        expected = TreeNode(0)
        self.sol.flatten(root)
        self.assertTrue(self.compare(expected, root))

if __name__ == "__main__":
    unittest.main()
