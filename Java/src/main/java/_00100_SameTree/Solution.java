package _00100_SameTree;

// Definition for a binary tree node.
class TreeNode {

    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {

    /**
     * Given the roots of two binary trees {@code p} and {@code q}, check if
     * they are the same.
     * <p>
     * Two binary trees are considered the same if they are structureally
     * identical, and the nodes have the same value.
     *
     * @param p root of first binary tree
     * @param q root of second binary tree
     * @return {@code true} if the binary trees are the same, or {@code false}
     * otherwise
     */
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // If both nodes are null, they are equal.
        if (p == null && q == null) {
            return true;
        }
        // If only one node is null then the other tree is deeper and the trees 
        // are not the same. If the values or two nodes are not the same, the 
        // trees are not the same.
        if (p == null || q == null || p.val != q.val) {
            return false;
        }

        // Traverse both trees together recursively an check if each node is the same.
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
