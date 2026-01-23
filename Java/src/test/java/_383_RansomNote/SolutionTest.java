package _383_RansomNote;

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
    private static int testCount = -1;

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
        testCount++;
        if (testCount != 0) {
            totalTime += runtime;
            System.out.println("Test " + testCount + ": " + (runtime / 1_000_000.00) + "ms");
        }
    }

    @AfterAll
    static void reportAverage() {
        System.out.println("Average runtime: " + (totalTime / testCount / 1_000_000.00) + " ms");
    }

    /* canConstruct version 1 */
    @RepeatedTest(2)
    @DisplayName("'a' cannot be constructed by use the letter 'b'")
    void a_b_v1() {
        assertFalse(sol.canConstruct("a", "b"));
    }

    @Test
    @DisplayName("'aa' cannot be constructed by using the letters 'ab'")
    void aa_ab_v1() {
        assertFalse(sol.canConstruct("aa", "ab"));
    }

    @Test
    @DisplayName("'aa' can be constructed by user the letters 'aab'")
    void aa_aab_v1() {
        assertTrue(sol.canConstruct("aa", "aab"));
    }

    /* canConstruct version 2 */
    @Test
    @DisplayName("'a' cannot be constructed by use the letter 'b'")
    void a_b_v2() {
        assertFalse(sol.canConstruct1("a", "b"));
    }

    @Test
    @DisplayName("'aa' cannot be constructed by using the letters 'ab'")
    void aa_ab_v2() {
        assertFalse(sol.canConstruct1("aa", "ab"));
    }

    @Test
    @DisplayName("'aa' can be constructed by user the letters 'aab'")
    void aa_aab_v2() {
        assertTrue(sol.canConstruct1("aa", "aab"));
    }
}
