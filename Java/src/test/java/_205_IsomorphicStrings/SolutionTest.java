package _205_IsomorphicStrings;

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

    /* isIsomorphic version 1 */
    @RepeatedTest(2)
    @DisplayName("'egg' and 'add' are isomorphic")
    void egg_add() {
        assertTrue(sol.isIsomorphic("egg", "add"));
    }

    @Test
    @DisplayName("'foo' and 'bar' are not isomorphic")
    void foo_bar() {
        assertFalse(sol.isIsomorphic("foo", "bar"));
    }

    @Test
    @DisplayName("'paper' and 'title' are isomorphic")
    void paper_title() {
        assertTrue(sol.isIsomorphic("paper", "title"));
    }


    /* isIsomorphic version 2 */
    @Test
    @DisplayName("'egg' and 'add' are isomorphic")
    void egg_add1() {
        assertTrue(sol.isIsomorphic1("egg", "add"));
    }

    @Test
    @DisplayName("'foo' and 'bar' are not isomorphic")
    void foo_bar1() {
        assertFalse(sol.isIsomorphic1("foo", "bar"));
    }

    @Test
    @DisplayName("'paper' and 'title' are isomorphic")
    void paper_title1() {
        assertTrue(sol.isIsomorphic1("paper", "title"));
    }
}
