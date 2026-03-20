# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Given a binary tree, find the lowest common ancestor (LCA) of two 
        given nodes in the tree.

        The lowest common ancestor is defined between two nodes `p` and `q` as 
        the lowest node in `T` that has both `p` and `q` as descendants (where 
        we allow **a node to be a descendant of itself**).”

        Args:
            root (TreeNode): root of a binary tree
            p (TreeNode): descendant node
            q (TreeNode): descendant node

        Returns:
            TreeNode: the lowest common ancestor
        """

        if not root or root == p or root == q:
            return root
        
        # Look for `p` and `q` in the left subtree.
        left = self.lowestCommonAncestor(root.left, p, q)
        # Look for `p` and `q` in the right subtree.
        right = self.lowestCommonAncestor(root.right, p, q)

        # If `p` and `q` are found in the left and right subtrees of this node,
        # then this node is the LCA
        if left and right:
            return root
        
        # Otherwise, the node that hasn't been found must be a decendant of the
        # node that has been found, so the node that has been found is the LCA.
        return left or right
    
import unittest

class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        root = TreeNode(3)
        node5 = TreeNode(5)
        node1 = TreeNode(1)
        node6 = TreeNode(6)
        node2 = TreeNode(2)
        node0 = TreeNode(0)
        node8 = TreeNode(8)
        node7 = TreeNode(7)
        node4 = TreeNode(4)

        root.left = node5
        root.right = node1
        node5.left = node6
        node5.right = node2
        node1.left = node0
        node1.right = node8
        node2.left = node7
        node2.right = node4

        p = node5
        q = node1
        expected = root
        actual = self.sol.lowestCommonAncestor(root, p, q)
        self.assertIs(expected, actual)

    def test_example2(self):
        root = TreeNode(3)
        node5 = TreeNode(5)
        node1 = TreeNode(1)
        node6 = TreeNode(6)
        node2 = TreeNode(2)
        node0 = TreeNode(0)
        node8 = TreeNode(8)
        node7 = TreeNode(7)
        node4 = TreeNode(4)

        root.left = node5
        root.right = node1
        node5.left = node6
        node5.right = node2
        node1.left = node0
        node1.right = node8
        node2.left = node7
        node2.right = node4

        p = node5
        q = node4
        expected = node5
        actual = self.sol.lowestCommonAncestor(root, p, q)
        self.assertIs(expected, actual)
    

if __name__ == "__main__":
    unittest.main()