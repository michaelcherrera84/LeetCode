package _00226_InvertBinaryTree;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

@SuppressWarnings("unused")
public class SolutionTest {

    public static long totalTime = 0;
    public static int count = 0;

    public long startTime;
    public Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
        startTime = System.currentTimeMillis();
    }

    @AfterEach
    void tearDown() {
        long runtime = System.currentTimeMillis() - startTime;
        if (count != 0) {
            totalTime += runtime;
        }
        System.out.println("Test " + count + ": " + runtime + " ms");
        count++;
    }

    @AfterAll
    static void averageTime() {
        if (count > 1) {
            System.out.println("Average Runtime: " + (totalTime / count) + " ms for " + (count - 1) + " tests");
        }
    }

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
    private boolean isSameTree(TreeNode p, TreeNode q) {
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

    @RepeatedTest(2)
    void randomTest1() {
        TreeNode root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(7, new TreeNode(6), new TreeNode(9)));

        TreeNode result = new TreeNode(4, new TreeNode(7, new TreeNode(9), new TreeNode(6)), new TreeNode(2, new TreeNode(3), new TreeNode(1)));

        assertTrue(isSameTree(sol.invertTree(root), result));
    }

    @Test
    void randomTest2() {
        TreeNode root = new TreeNode(2, new TreeNode(1), new TreeNode(3));
        TreeNode result = new TreeNode(2, new TreeNode(3), new TreeNode(1));

        assertTrue(isSameTree(sol.invertTree(root), result));
    }

    @Test
    void empty_list_returns_null() {
        assertNull(sol.invertTree(null));
    }
}
