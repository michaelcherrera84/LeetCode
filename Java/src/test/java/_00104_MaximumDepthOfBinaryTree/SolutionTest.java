package _00104_MaximumDepthOfBinaryTree;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
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
        TreeNode root = new TreeNode(
            3, new TreeNode(9), new TreeNode(
                20, new TreeNode(15), new TreeNode(7)));

        assertEquals(3, sol.maxDepth(root));
    }

    @Test
    @DisplayName("Tree has no left depth but has right depth")
    void example2() {
        TreeNode root = new TreeNode(1, null, new TreeNode(2));

        assertEquals(2, sol.maxDepth(root));
    }

    @Test
    void empty_tree_has_0_depth() {
        assertEquals(0, sol.maxDepth(null));
    }

    @Test
    void tree_has_left_depth_but_no_right() {
        TreeNode root = new TreeNode(1, new TreeNode(2), null);

        assertEquals(2, sol.maxDepth(root));
    }
}
