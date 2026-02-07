package _222_CountCompleteTreeNodes;

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
        TreeNode root = new TreeNode(1, new TreeNode(2, new TreeNode(4), new TreeNode(5)), new TreeNode(3, new TreeNode(6), null));

        assertEquals(6, sol.countNodes(root));
    }

    @Test
    @DisplayName("Empty tree has no nodes")
    void example2() {
        assertEquals(0, sol.countNodes(null));
    }

    @Test
    @DisplayName("A tree with 1 node has 1 node")
    void example3() {
        assertEquals(1, sol.countNodes(new TreeNode(1)));
    }

    @Test
    @DisplayName("A perfect tree with 3 nodes has 3 nodes")
    void perfectTree() {
        TreeNode root = new TreeNode(1, new TreeNode(2), new TreeNode(3));
        assertEquals(3, sol.countNodes(root));
    }
}
