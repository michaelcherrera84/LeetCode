package _00202_HappyNumber;

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

    private static long totalTime = 0;
    private static int testCount = 0;

    private long startTime = 0;
    private Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
        startTime = System.nanoTime();
    }

    @AfterEach
    void tearDown() {
        long runtime = System.nanoTime() - startTime;
        totalTime += runtime;
        System.out.println("Test " + testCount + ": " + (runtime / 1_000_000.00) + "ms");
        testCount++;
    }

    @AfterAll
    static void reportAverage() {
        System.out.println("Average runtime: " + (totalTime / testCount / 1_000_000.00) + " ms");
    }

    @RepeatedTest(2)
    @DisplayName("19 is a happy number")
    void _19() {
        assertTrue(sol.isHappy(19));
    }

    @Test
    @DisplayName("2 is not a happy number")
    void _2() {
        assertFalse(sol.isHappy(2));
    }

    @Test
    @DisplayName("19 is a happy number")
    void _19_v2() {
        assertTrue(sol.isHappy1(19));
    }

    @Test
    @DisplayName("2 is not a happy number")
    void _2_v2() {
        assertFalse(sol.isHappy1(2));
    }
}