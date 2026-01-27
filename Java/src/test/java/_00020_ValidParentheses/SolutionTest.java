package _00020_ValidParentheses;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;

public class SolutionTest {

    private static long totalTime;
    private static int count;

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
        totalTime += runtime;
        System.out.println("Test " + count + ": " + runtime + " ms");
        count++;
    }

    @AfterAll
    static void averageTime() {
        System.out.println("Average runtime: " + (totalTime / count) + " ms");
    }

    @RepeatedTest(2)
    @DisplayName("1")
    void randomTest1() {
        assertTrue(sol.isValid("()"));
    }

    @Test
    @DisplayName("2")
    void randomTest2() {
        assertTrue(sol.isValid("()[]{}"));
    }

    @Test
    @DisplayName("3")
    void randomTest3() {
        assertFalse(sol.isValid("(]"));
    }

    @Test
    @DisplayName("4")
    void randomTest4() {
        assertTrue(sol.isValid("([])"));
    }

    @Test
    @DisplayName("5")
    void randomTest5() {
        assertFalse(sol.isValid("([)]"));
    }

    @Test
    @DisplayName("6")
    void single_character_is_invalid() {
        assertFalse(sol.isValid("("));
    }

    @Test
    @DisplayName("7")
    void empty_string_is_invalid() {
        assertFalse(sol.isValid(""));
    }

    @Test
    @DisplayName("8")
    void no_closing_brackets_is_invalid() {
        assertFalse(sol.isValid("(("));
    }

    @Test
    @DisplayName("9")
    void only_closing_brackets_is_invalid() {
        assertFalse(sol.isValid("))"));
    }
}
