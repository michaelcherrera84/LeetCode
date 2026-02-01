package _00226_InvertBinaryTree;

/**
 * Definition for a binary tree node.
 */
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
     * Given the {@code root} of a binary tree, invert the tree, and return
     * <i>its root</i>.
     *
     * @param root the root of a binary tree
     * @return the root of the inverted tree
     */
    public TreeNode invertTree(TreeNode root) {

        // If root is null, we've reached the bottom of the tree, or there is no tree.
        if (root == null) {
            return null;
        }

        // Go left until we until we get to the bottom of the tree.
        invertTree(root.left);

        // Swap the left and right nodes.
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;

        // Since the left and right nodes were swapped, go left again.
        invertTree(root.left);

        return root;
    }
}
