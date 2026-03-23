package _00098_ValidateBinarySearchTree;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.ArrayDeque;
import java.util.Deque;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() { sol = new Solution(); }

    private TreeNode buildTree(Integer[] input) {
        TreeNode root = new TreeNode(input[0]);
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.add(root);
        int i = 1;
        int n = input.length;

        while (!queue.isEmpty() && i < n) {
            TreeNode curr = queue.pollFirst();

            if (i < n && input[i] != null) {
                curr.left = new TreeNode(input[i]);
                queue.add(curr.left);
            }
            i++;

            if (i < n && input[i] != null) {
                curr.right = new TreeNode(input[i]);
                queue.add(curr.right);
            }
            i++;
        }

        return root;
    }

    @Test
    void example1() {
        Integer[] input = { 2, 1, 3 };
        TreeNode root = buildTree(input);
        assertTrue(sol.isValidBST(root));
    }

    @Test
    void example2() {
        Integer[] input = { 5, 1, 4, null, null, 3, 6 };
        TreeNode root = buildTree(input);
        assertFalse(sol.isValidBST(root));
    }
}
