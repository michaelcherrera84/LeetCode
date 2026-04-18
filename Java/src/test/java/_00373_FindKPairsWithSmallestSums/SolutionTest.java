package _00373_FindKPairsWithSmallestSums;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() { sol = new Solution(); }

    @Test
    void example1() {
        int[] nums1 = { 1, 7, 11 };
        int[] nums2 = { 2, 4, 6 };
        int k = 3;
        int[][] expected = {
                { 1, 2 },
                { 1, 4 },
                { 1, 6 }
        };
        List<List<Integer>> actual = sol.kSmallestPairs(nums1, nums2, k);
        List<List<Integer>> expectedToList = Arrays.stream(expected)
            .map(row -> Arrays.stream(row).boxed().collect(Collectors.toList()))
            .collect(Collectors.toList());
        assertEquals(expectedToList, actual);
    }

    @Test
    void example2() {
        int[] nums1 = { 1, 1, 2 };
        int[] nums2 = { 1, 2, 3 };
        int k = 2;
        int[][] expected = {
                { 1, 1 },
                { 1, 1 }
        };
        List<List<Integer>> actual = sol.kSmallestPairs(nums1, nums2, k);
        List<List<Integer>> expectedToList = Arrays.stream(expected)
            .map(row -> Arrays.stream(row).boxed().collect(Collectors.toList()))
            .collect(Collectors.toList());
        assertEquals(expectedToList, actual);
    }
}
