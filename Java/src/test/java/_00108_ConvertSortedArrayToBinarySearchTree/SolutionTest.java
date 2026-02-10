package _00108_ConvertSortedArrayToBinarySearchTree;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
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
    void example1() {
        int[] nums = {-10, -3, 0, 5, 9};
        var expected = new TreeNode(
                0,
                new TreeNode(
                        -10,
                        null,
                        new TreeNode(-3)),
                new TreeNode(
                        5,
                        null,
                        new TreeNode(9)));

        assertTrue(isSameTree(expected, sol.sortedArrayToBST(nums)));
    }

    @Test
    void example2() {
        int[] nums = {1, 3};
        var expected = new TreeNode(1, null, new TreeNode(3));

        assertTrue(isSameTree(expected, sol.sortedArrayToBST(nums)));
    }
}
