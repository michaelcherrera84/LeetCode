package _00530_MinimumAbsoluteDifferenceInBST;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

@SuppressWarnings("unused")
public class SolutionTest {

    private static long totalTime = 0;
    private static int count = 0;

    private Solution sol;
    private long start;

    @BeforeEach
    void setUp() {
        sol = new Solution();
        start = System.currentTimeMillis();
    }

    @AfterEach
    void tearDown() {
        long runtime = System.currentTimeMillis() - start;
        System.out.println("Test " + count + ": " + runtime + " ms");
        if (count > 0) {
            totalTime += runtime;
        }
        count++;
    }

    @AfterAll
    static void averageTime() {
        System.out.println("Average runtime: " + (totalTime / (count - 1)) + " ms");
    }

    @RepeatedTest(2)
    void example1() {
        var root = new TreeNode(4, new TreeNode(2, new TreeNode(1), new TreeNode(3)), new TreeNode(6));
        assertEquals(1, sol.getMinimumDifference(root));
    }

    @Test
    void example2() {
        var root = new TreeNode(1, new TreeNode(0), new TreeNode(48, new TreeNode(12), new TreeNode(49)));
        assertEquals(1, sol.getMinimumDifference(root));
    }

    @Test
    @DisplayName("Difference of [100000, 0] is 100000")
    void two_nodes_with_zero() {
        var root = new TreeNode(100_000, new TreeNode(0), null);
        assertEquals(100_000, sol.getMinimumDifference(root));
    }
}
