package _00219_ContainsDuplicateII;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

@SuppressWarnings("unused")
public class SolutionTest {

    private static long totalTime;
    private static long testCount;

    private long startTime;
    private Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
        startTime = System.currentTimeMillis();
    }

    @AfterEach
    void tearDown() {
        long runtime = System.currentTimeMillis() - startTime;
        System.out.println("Test " + testCount + ": " + runtime + " ms");
        testCount++;
    }

    @AfterAll
    static void reportAverage() {
        System.out.println("Average Runtime: " + (totalTime / testCount) + " ms");
    }

    @RepeatedTest(2)
    @DisplayName("[1,2,3,1] contains two indices with equal values not more than 3 apart.")
    void _1_2_3_1__3() {
        assertTrue(sol.containsNearbyDuplicate(new int[] {1, 2, 3, 1}, 3));
    }

    @Test
    @DisplayName("[1,0,1,1] contains two indices with equal values not more than 1 apart.")
    void _1_0_1_1__1() {
        assertTrue(sol.containsNearbyDuplicate(new int[] {1, 0, 1, 1}, 1));
    }

    @Test
    @DisplayName("[1,2,3,1,2,3] does not contain two indices with equal values not more than 2 apart.")
    void _1_2_3_1_2_3__2() {
        assertFalse(sol.containsNearbyDuplicate(new int[] {1, 2, 3, 1, 2, 3}, 2));
    }
}
