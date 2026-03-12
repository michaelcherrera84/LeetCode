package _00224_BasicCalculator;

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
        String s = "1 + 1";
        int expected = 2;
        int actual = sol.calculate(s);
        assertEquals(expected, actual);
    }

    @Test
    void example2() {
        String s = " 2-1 + 2";
        int expected = 3;
        int actual = sol.calculate(s);
        assertEquals(expected, actual);
    }

    @Test
    void example3() {
        String s = "(1+(4+5+2)-3)+(6+8)";
        int expected = 23;
        int actual = sol.calculate(s);
        assertEquals(expected, actual);
    }
}
