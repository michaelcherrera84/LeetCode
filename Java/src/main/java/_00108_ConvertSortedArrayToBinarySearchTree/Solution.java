package _00108_ConvertSortedArrayToBinarySearchTree;

/**
 * Definition for a binary tree node.
 */
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

public class Solution {

    /**
     * Given an integer array {@code nums} where the elements are sorted in
     * <b>ascending order</b> convert <i>it to a height-balanced binary search
     * tree</i>.
     *
     * @param nums the integer array
     * @return the root of the binary search tree
     */
    public TreeNode sortedArrayToBST(int[] nums) {
        return buildTree(0, nums.length - 1, nums);
    }

    /**
     * Build the BST by repeatedly dividing the array, using the lower half for
     * the left side of the sub-tree and the upper half for the right side of
     * the sub-tree.
     *
     * @param left pointer to the lowest value of the sub-array
     * @param right pointer to the highest value of the sub-array
     * @param nums the array
     * @return the root of the current sub-tree
     */
    private TreeNode buildTree(int left, int right, int[] nums) {
        // If the left pointer is greater than the right pointer, the array has 
        // no values.
        if (left > right) {
            return null;
        }

        int mid = (left + right) >> 1;

        // Assign the middle value to this node
        TreeNode node = new TreeNode(nums[mid]);

        // Use the lower half of the array for the left side of the tree.
        node.left = buildTree(left, mid - 1, nums);
        // Use the upper half of the array for the right side of the tree.
        node.right = buildTree(mid + 1, right, nums);

        return node;
    }
}
