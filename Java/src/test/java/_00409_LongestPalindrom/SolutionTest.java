package _00409_LongestPalindrom;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() {
        sol = new Solution();
    }

    @Test
    void example1() {
        String s = "abccccdd";
        int expected = 7;
        int actual = sol.longestPalindrome(s);
        assertEquals(expected, actual);
    }

    @Test
    void example2() {
        String s = "z";
        int expected = 1;
        int actual = sol.longestPalindrome(s);
        assertEquals(expected, actual);
    }
}
