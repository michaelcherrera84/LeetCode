from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Given the `root` of a binary search tree, and an integer `k`, return
        *the* `kth` *smallest value **(1-indexed)** of all the values of the
        nodes in the tree*.

        Args:
            root (Optional[TreeNode]): the root of a binary tree
            k (int): the integer index

        Returns:
            int: the `kth` smalles value of the BST
        """

        def find(node, i, res):
            """Find the kth node using inorder traversal and return its value

            Args:
                node (TreeNode): the current node
                i (int): the current inorder "index" of the BST
                res (int): the value of kth node or `None`

            Returns:
                _type_: the value of the kth node (`res`)
            """

            if not node:
                return None

            # Go left while there are left nodes. The smallest value node is the
            # last left node in the first path.
            res = find(node.left, i, res)

            # If res has already been found, no further seach is necessary.
            if res == None:
                # Here, we have found the smallest value.
                i[0] += 1 # Increment the count until the kth value is found.
                if i[0] == k:
                    return node.val
                res = find(node.right, i, res)
            return res

        return find(root, [0], None)


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        k = 1
        expected = 1
        actual = self.sol.kthSmallest(root, k)
        self.assertEqual(expected, actual)

    def test_example2(self):
        root = TreeNode(
            5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)
        )
        k = 3
        expected = 3
        actual = self.sol.kthSmallest(root, k)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
