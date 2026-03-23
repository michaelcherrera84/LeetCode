from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Given the `root` of a binary tree, *determine if it is a valid binary
        search tree (BST)*.

        A **valid BST** is defined as follows:

        - The left subtree of a node contains only nodes with keys **strictly
        less than** the node's key.
        - The right subtree of a node contains only nodes with keys **strictly
        greater than** the node's key.
        - Both the left and right subtrees must also be binary search trees.

        Args:
            root (Optional[TreeNode]): The root of a binary search tree

        Returns:
            bool: `True` if the BST is valid, or `False` otherwise
        """

        curr = root  # current node being validated
        prev = None  # previous validated node

        # While there are nodes left to be validated, traverse the tree using a
        # Morris inorder traversal.
        while curr:
            # If there is a node to the left of the current node...
            if not curr.left:
                # If we have already validated a node, then this node's value
                # should be greater than the previous node's value.
                if prev and curr.val <= prev.val:
                    return False
                # Otherwise, this node is valid. Set this node as the previous
                # node.
                prev = curr
                # Advance to right child (which may be a threaded link back to 
                # an ancestor).
                curr = curr.right
            else:
                # The left node should be a predecessor to the current node.
                pred = curr.left

                # While predecessor has right nodes that are not the current 
                # node, advance pred to the right.
                while pred.right and pred.right is not curr:
                    pred = pred.right

                # If there is no right node, temporarily set the predecessor's
                # right node to the current node, which should be the next node
                # after this predecessor in order.
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                # Otherwise, the right node is the current node. Now this
                # predecessor's right node should be returned to its original
                # value of `None`.
                else:
                    pred.right = None
                    # The current node's value should be greater than the 
                    # previous node's value.
                    if prev and curr.val <= prev.val:
                        return False
                    prev = curr
                    curr = curr.right

        return True


import unittest
from collections import deque
from typing import List


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def build_tree_from_array(self, nums: List[Optional[int]]) -> Optional[TreeNode]:
        """
        Builds a binary tree from a LeetCode-style level order array.
        """
        if not nums:
            return None

        root = TreeNode(nums[0])
        queue = deque([root])
        i = 1
        n = len(nums)

        while queue and i < n:
            curr = queue.popleft()

            # Process left child
            if i < n and nums[i] is not None:
                curr.left = TreeNode(nums[i])
                queue.append(curr.left)
            i += 1

            # Process right child
            if i < n and nums[i] is not None:
                curr.right = TreeNode(nums[i])
                queue.append(curr.right)
            i += 1

        return root

    def test_example1(self):
        input = [2, 1, 3]
        root = self.build_tree_from_array(input)
        self.assertTrue(self.sol.isValidBST(root))

    def test_example2(self):
        input = [5, 1, 4, None, None, 3, 6]
        root = self.build_tree_from_array(input)
        self.assertFalse(self.sol.isValidBST(root))

    def test_example3(self):
        input = [2, 2, 2]
        root = self.build_tree_from_array(input)
        self.assertFalse(self.sol.isValidBST(root))

    def test_example4(self):
        input = [1, 1, 3]
        root = self.build_tree_from_array(input)
        self.assertFalse(self.sol.isValidBST(root))

    def test_all_left_valid(self):
        input = [3, 2, None, 1]
        root = self.build_tree_from_array(input)
        self.assertTrue(self.sol.isValidBST(root))

    def test_all_left_invalid(self):
        input = [3, 5, None, 1]
        root = self.build_tree_from_array(input)
        self.assertFalse(self.sol.isValidBST(root))

    def test_left_then_one_right(self):
        input = [4, 3, None, 1, None, None, 2]
        root = self.build_tree_from_array(input)
        self.assertTrue(self.sol.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
