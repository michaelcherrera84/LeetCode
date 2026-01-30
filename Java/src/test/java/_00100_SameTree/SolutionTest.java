package _00100_SameTree;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertFalse;
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

    @RepeatedTest(2)
    void example1() {
        TreeNode p = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        TreeNode q = new TreeNode(1, new TreeNode(2), new TreeNode(3));

        assertTrue(sol.isSameTree(p, q));
    }

    @Test
    void example2() {
        TreeNode p = new TreeNode(1, new TreeNode(2), null);
        TreeNode q = new TreeNode(1, null, new TreeNode(2));

        assertFalse(sol.isSameTree(p, q));
    }

    @Test
    void example3() {
        TreeNode p = new TreeNode(1, new TreeNode(2), new TreeNode(1));
        TreeNode q = new TreeNode(1, new TreeNode(1), new TreeNode(2));

        assertFalse(sol.isSameTree(p, q));
    }

    @Test
    void both_list_empty_are_the_same() {
        assertTrue(sol.isSameTree(null, null));
    }

    @Test 
    void one_list_empty_is_not_the_same() {
        TreeNode p = new TreeNode(1, new TreeNode(2), new TreeNode(1));

        assertFalse(sol.isSameTree(p, null));
        assertFalse(sol.isSameTree(null, p));
    }
}
