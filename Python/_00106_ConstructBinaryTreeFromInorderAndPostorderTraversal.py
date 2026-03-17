from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Given two integer arrays `inorder` and `postorder` where `inorder` is
        the inorder traversal of a binary tree and `postorder` is the postorder
        traversal of the same tree, construct and return *the binary tree*.

        Args:
            inorder (List[int]): the inorder traversal of the binary tree
            postorder (List[int]): the postorder traversal of the binary tree

        Returns:
            Optional[TreeNode]: the root of the binary tree
        """

        inorder_map = {val: i for i, val in enumerate(inorder)}
        i = -1

        def build(start, end):
            """Build a binary tree from the postorder and inorder traversals.

            Args:
                start (int): the beginning of this subtree's range in the
                inorder traversal
                end (int): the end of this subtree's range in the inorder
                traversal

            Returns:
                TreeNode: the binary tree
            """

            # There are no more nodes in this subtree.
            if start > end:
                return None
            
            nonlocal i

            # The root is always the next unused value in the postorder
            # traversal from the end of the array.
            root = TreeNode(postorder[i])
            i -= 1

            # Find the position of this root in the indorder traversal. Values
            # with higher indices belong to the right subtree. Values with lower
            # indices belong to the left subtree.
            mid = inorder_map[root.val]

            # Build the tree beginning with the right subtree.
            root.right = build(mid + 1, end)
            root.left = build(start, mid - 1)

            return root

        return build(0, len(postorder) - 1)


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def compare(self, t1, t2):
        if t1 and not t2 or t2 and not t1:
            return False
        if not t1 and not t2:
            return True

        if t1.val != t2.val:
            return False

        return self.compare(t1.left, t2.left) and self.compare(t1.right, t2.right)

    def test_example1(self):
        inorder = [9, 3, 15, 20, 7]
        postorder = [9, 15, 7, 20, 3]

        expected = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        actual = self.sol.buildTree(inorder, postorder)

        self.assertTrue(self.compare(expected, actual))

    def test_example2(self):
        inorder = [-1]
        postorder = [-1]

        expected = TreeNode(-1)
        actual = self.sol.buildTree(inorder, postorder)

        self.assertTrue(self.compare(expected, actual))

if __name__ == "__main__":
    unittest.main()
