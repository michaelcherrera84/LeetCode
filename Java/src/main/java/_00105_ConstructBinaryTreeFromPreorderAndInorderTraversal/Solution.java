package _00105_ConstructBinaryTreeFromPreorderAndInorderTraversal;

import java.util.HashMap;
import java.util.Map;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) { this.val = val; }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {

    /**
     * Given two integer arrays `preorder` and `inorder` where `preorder` is the
     * preorder traversal of a binary tree and `inorder` is the inorder
     * traversal of the same tree, construct and return *the binary tree*.
     *
     * @param preorder preorder traversal of a binary tree
     * @param inorder  inorder traversal of a binary tree
     * @return the binary tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Delegate to an inner class instance so that mutable traversal state
        // (the preorder index and inorder map) is scoped to a single call and
        // automatically reset for every fresh invocation.
        return new Build(preorder, inorder).buildTree(0, preorder.length - 1);
    }

    /**
     * Encapsulates the mutable state needed during tree construction:
     * <ul>
     * <li>A map from node value → its index in the inorder array, for O(1) root
     * lookups.</li>
     * <li>A cursor {@code i} that advances through the preorder array
     * left-to-right, always pointing at the root of the subtree currently being
     * built.</li>
     * </ul>
     */
    private class Build {
        /** Maps each value to its position in the inorder traversal. */
        Map<Integer, Integer> inorder = new HashMap<>();
        /** The preorder traversal array; consumed front-to-back via {@code i}. */
        int[] preorder;
        /**
         * Cursor into {@code preorder}. Starts at 0 and increments once per node
         * created. Because preorder visits a root before either of its subtrees,
         * simply advancing this cursor in the same recursive order faithfully
         * reconstructs each root in turn.
         */
        int i = 0;

        public Build(int[] preorder, int[] inorder) {
            this.preorder = preorder;
            for (int i = 0; i < inorder.length; i++) {
                this.inorder.put(inorder[i], i);
            }
        }

        /**
         * Recursively builds the subtree whose nodes occupy
         * {@code inorder[start..end]}.
         *
         * <p>
         * Each call:
         * <ol>
         * <li>Consumes {@code preorder[i]} as the subtree root (preorder guarantees
         * this).</li>
         * <li>Looks up that value in the inorder map to find {@code mid} — the
         * index that splits the remaining inorder range into a left portion
         * ({@code start..mid-1}) and a right portion ({@code mid+1..end}).</li>
         * <li>Recurses left before right, which keeps the preorder cursor {@code i}
         * advancing in the correct front-to-back order.</li>
         * </ol>
         *
         * @param start first index (inclusive) of this subtree's range in the
         *              inorder array
         * @param end   last index (inclusive) of this subtree's range in the
         *              inorder array
         * @return the root {@link TreeNode} of the constructed subtree, or
         *         {@code null} if the range is empty
         */
        public TreeNode buildTree(int start, int end) {
            // Empty range — no nodes left in this subtree.
            if (start > end)
                return null;

            // The next value in preorder is always the root of the current subtree.
            TreeNode root = new TreeNode(preorder[i++]);

            // Find where this root sits in the inorder array.
            // Everything to its left belongs to the left subtree; everything to its
            // right belongs to the right subtree.
            int mid = inorder.get(root.val);

            // Build the left subtree first — this is critical. Because we're walking
            // the preorder array with a shared cursor, we must recurse in the same
            // order preorder visits nodes: left subtree entirely before right subtree.
            root.left = buildTree(start, mid - 1);
            root.right = buildTree(mid + 1, end);

            return root;
        }
    }
}
