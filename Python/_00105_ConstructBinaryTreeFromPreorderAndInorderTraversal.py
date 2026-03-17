from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Given two integer arrays `preorder` and `inorder` where `preorder` is
        the preorder traversal of a binary tree and `inorder` is the inorder
        traversal of the same tree, construct and return *the binary tree*.

        Args:
            preorder (List[int]): preorder traversal of a binary tree
            inorder (List[int]): inorder traversal of a binary tree

        Returns:
            Optional[TreeNode]: the binary tree
        """

        # Map the inorder traversal to its indices.
        inorder_map = {val: i for i, val in enumerate(inorder)}
        i = 0  # current index of the preorder traversal

        def build(start, end):
            """Build a binary tree from the preorder and inorder traversals of
            the tree.

            Args:
                start (int): beginning of this subtree's range in the inorder
                traversal
                end (int): end of this subtree's range in the inorder traversal

            Returns:
                TreeNode: the root of the binary tree
            """

            # If there are no nodes left in this subtree, return.
            if start > end:
                return None

            nonlocal i

            # The root of each subtree is always the next unused value in the
            # preorder traversal.
            root = TreeNode(preorder[i])
            i += 1  # Advance to the next value in preorder.

            # Find where this root is in the inorder array. Nodes with a lower
            # index belong to the left subtree. Nodes with a higher index belong
            # to the right subtree.
            mid = inorder_map[root.val]

            # Build the left side of the tree and then the right side of the tree.
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def compare(self, t1: "TreeNode | None", t2: "TreeNode | None") -> bool:
        if not t1 and t2 or not t2 and t1:
            return False
        elif not t1 and not t2:
            return True

        assert t1 and t2
        if t1.val != t2.val:
            return False

        return self.compare(t1.left, t2.left) and self.compare(t1.right, t2.right)

    def test_example1(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]

        expected = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        actual = self.sol.buildTree(preorder, inorder)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        preorder = [-1]
        inorder = [-1]

        expected = TreeNode(-1)
        actual = self.sol.buildTree(preorder, inorder)

        self.assertTrue(self.compare(expected, actual))


if __name__ == "__main__":
    unittest.main()
