package _00215_KthLargestElementInAnArray;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() { sol = new Solution(); }

    @Test
    void example1() {
        int[] nums = { 3, 2, 1, 5, 6, 4 };
        int k = 2;
        int expected = 5;
        int actual = sol.findKthLargest(nums, k);
        assertEquals(expected, actual);
    }

    @Test
    void example2() {
        int[] nums = { 3, 2, 3, 1, 2, 4, 5, 5, 6 };
        int k = 4;
        int expected = 4;
        int actual = sol.findKthLargest(nums, k);
        assertEquals(expected, actual);
    }
}
