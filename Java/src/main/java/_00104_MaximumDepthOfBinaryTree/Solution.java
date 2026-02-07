package _00104_MaximumDepthOfBinaryTree;

@SuppressWarnings("unused")
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

@SuppressWarnings("unused")
public class Solution {

    /**
     * Given the {@code root} of a binary tree, return <i>it's maximum
     * depth.</i>
     * <p>
     * A binary tree's <b>maximum depth</b> is the number of nodes along the
     * longest path from the root node down to the farthest leaf node.
     *
     * @param root the root node of the binary tree
     * @return the maximum depth of the binary tree
     */
    int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        // return maxDepth(root, 1, 1);

        // Treverse the tree recursively until reaching the bottom. Then add 1 
        // row for each level counting back to the root.
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

    /**
     * Helper method tracks the depth of each node, and records a new max depth
     * if the current depth is deeper then max.
     *
     * @param node the current node
     * @param depth the depth of the current node
     * @param max the max depth of the tree
     * @return the max depth of the tree
     */
    private int maxDepth(TreeNode node, int depth, int max) {
        // Base case: if the current node is null the max stays the same.
        if (node == null) {
            return max;
        }

        // If the current depth is deeper than max, update max to the current depth.
        if (depth > max) {
            max = depth;
        }

        // Go left. The depth will be 1 deeper than the current depth.
        max = maxDepth(node.left, depth + 1, max);
        // Go right. The depth will be 1 deeper than the current depth.
        max = maxDepth(node.right, depth + 1, max);

        // Return the deepest depth found.
        return max;
    }
}
