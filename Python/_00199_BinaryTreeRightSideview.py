from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Given the `root` of a binary tree, imagine yourself standing on the
        **right side** of it, return *the values of the nodes you can see
        ordered from top to bottom*.

        Args:
            root (Optional[TreeNode]): the root of a binary tree

        Returns:
            List[int]: the values of the nodes that can be seen from the right,
            ordered from top to bottom
        """

        if not root:
            return []
        
        res = []
        
        # Traverse the tree, right side first.
        def reverse_preorder(node, level):
            if not node:
                return

            # Build the list of viewable nodes. Since we are traversing the right
            # side of the tree first, the first node we see at each level is the
            # node that is viewable from the right side.
            if len(res) == level:
                res.append(node.val)

            reverse_preorder(node.right, level + 1)
            reverse_preorder(node.left, level + 1)
        
        reverse_preorder(root, 0)

        return res


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        expected = [1, 3, 4]
        actual = self.sol.rightSideView(root)
        self.assertEqual(expected, actual)

    def test_example2(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
        expected = [1, 3, 4, 5]
        actual = self.sol.rightSideView(root)
        self.assertEqual(expected, actual)

    def test_example3(self):
        root = TreeNode(1, None, TreeNode(3))
        expected = [1, 3]
        actual = self.sol.rightSideView(root)
        self.assertEqual(expected, actual)

    def test_example4(self):
        root = None
        expected = []
        actual = self.sol.rightSideView(root)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
