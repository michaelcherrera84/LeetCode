package _00637_AverageOfLevelsInBinaryTree;

import java.util.List;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertEquals;
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
        TreeNode root = new TreeNode(3, new TreeNode(9), new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        List<Double> expected = List.of(3.0, 14.50, 11.0);
        List<Double> actual = sol.averageOfLevels(root);
        double delta = 1e-5;

        assertEquals(expected.size(), actual.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i), actual.get(i), delta);
        }
    }

    @Test
    void example2() {
        TreeNode root = new TreeNode(3, new TreeNode(9, new TreeNode(15), new TreeNode(7)), new TreeNode(20));
        List<Double> expected = List.of(3.0, 14.50, 11.0);
        List<Double> actual = sol.averageOfLevels(root);
        double delta = 1e-5;

        assertEquals(expected.size(), actual.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i), actual.get(i), delta);
        }
    }
}
