package _00399_EvaluateDivision;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() { sol = new Solution(); }

    @Test
    void example1() {
        List<List<String>> equations = List.of(
                List.of("a", "b"),
                List.of("b", "c"));
        double[] values = new double[] { 2.0, 3.0 };
        List<List<String>> queries = List.of(
                List.of("a", "c"),
                List.of("b", "a"),
                List.of("a", "e"),
                List.of("a", "a"),
                List.of("x", "x"));
        double[] expected = new double[] { 6.00000, 0.50000, -1.00000, 1.00000, -1.00000 };
        double[] actual = sol.calcEquation(equations, values, queries);
        assertArrayEquals(expected, actual);
    }

    @Test
    void example2() {
        List<List<String>> equations = List.of(
                List.of("a", "b"),
                List.of("b", "c"),
                List.of("bc", "cd"));
        double[] values = new double[] { 1.5, 2.5, 5.0 };
        List<List<String>> queries = List.of(
                List.of("a", "c"),
                List.of("c", "b"),
                List.of("bc", "cd"),
                List.of("cd", "bc"));
        double[] expected = new double[] { 3.75000, 0.40000, 5.00000, 0.20000 };
        double[] actual = sol.calcEquation(equations, values, queries);
        assertArrayEquals(expected, actual);
    }

    @Test
    void example3() {
        List<List<String>> equations = List.of(
                List.of("a", "b"));
        double[] values = new double[] { 0.5 };
        List<List<String>> queries = List.of(
                List.of("a", "b"),
                List.of("b", "a"),
                List.of("a", "c"),
                List.of("x", "y"));
        double[] expected = new double[] { 0.50000, 2.00000, -1.00000, -1.00000 };
        double[] actual = sol.calcEquation(equations, values, queries);
        assertArrayEquals(expected, actual);
    }

    @Test
    void example4() {
        List<List<String>> equations = List.of(
                List.of("x1", "x2"),
                List.of("x2", "x3"),
                List.of("x3", "x4"),
                List.of("x4", "x5"));
        double[] values = new double[] { 3.0, 4.0, 5.0, 6.0 };
        List<List<String>> queries = List.of(
                List.of("x1", "x5"),
                List.of("x5", "x2"),
                List.of("x2", "x4"),
                List.of("x2", "x2"),
                List.of("x2", "x9"),
                List.of("x9", "x9"));
        double[] expected = new double[] { 360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000 };
        double[] actual = sol.calcEquation(equations, values, queries);
        for (int i = 0; i < expected.length; i++) {
            assertEquals(expected[i], actual[i], 0.00001);
        }
    }
}
