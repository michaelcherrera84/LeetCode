package _00057_InsertInterval;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

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
        int[][] intervals = { { 1, 3 }, { 6, 9 } };
        int[] newInterval = { 2, 5 };
        int[][] expected = { { 1, 5 }, { 6, 9 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }

    @Test
    void example2() {
        int[][] intervals = { { 1, 2 }, { 3, 4 }, { 6, 7 }, { 8, 10 }, { 12, 16 } };
        int[] newInterval = { 4, 8 };
        int[][] expected = { { 1, 2 }, { 3, 10 }, { 12, 16 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }

    @Test
    void empty_intervals() {
        int[][] intervals = {};
        int[] newInterval = { 4, 8 };
        int[][] expected = { { 4, 8 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }

    @Test
    void newInterval_overlap_all() {
        int[][] intervals = { { 2, 3 }, { 4, 5 } };
        int[] newInterval = { 1, 6 };
        int[][] expected = { { 1, 6 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }

    @Test
    void newInterval_begging_no_overlap() {
        int[][] intervals = { { 3, 4 }, { 5, 6 } };
        int[] newInterval = { 1, 2 };
        int[][] expected = { { 1, 2 }, { 3, 4 }, { 5, 6 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }

    @Test
    void newInterval_end_overlap() {
        int[][] intervals = { { 2, 3 }, { 4, 5 } };
        int[] newInterval = { 5, 6 };
        int[][] expected = { { 2, 3 }, { 4, 6 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }

    @Test
    void newInterval_end_no_overlap() {
        int[][] intervals = { { 2, 3 }, { 4, 5 } };
        int[] newInterval = { 6, 7 };
        int[][] expected = { { 2, 3 }, { 4, 5 }, { 6, 7 } };
        int[][] actual = sol.insert(intervals, newInterval);
        assertArrayEquals(expected, actual);
    }
}
