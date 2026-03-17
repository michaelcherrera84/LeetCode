package _00105_ConstructBinaryTreeFromPreorderAndInorderTraversal;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() { sol = new Solution(); }

    private boolean compare(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 != null || t1 != null && t2 == null)
            return false;
        if (t1 == null && t2 == null)
            return true;

        if (t1.val != t2.val)
            return false;

        return compare(t1.left, t2.left) && compare(t1.right, t2.right);
    }

    @Test
    void example1() {
        int[] preorder = { 3, 9, 20, 15, 7 };
        int[] inorder = { 9, 3, 15, 20, 7 };

        TreeNode expected = new TreeNode(
                3,
                new TreeNode(9),
                new TreeNode(
                        20,
                        new TreeNode(15),
                        new TreeNode(7)));
        TreeNode actual = sol.buildTree(preorder, inorder);

        assertTrue(compare(expected, actual));
    }
}
