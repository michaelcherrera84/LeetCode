package _00074_SearchA2DMatrix;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    Solution sol;

    @BeforeEach
    void setUp() { sol = new Solution(); }

    @Test
    void example1() { 
        int[][] matrix = { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 } }; 
        boolean output = sol.searchMatrix(matrix, 3);
        assertTrue(output);
    };

    @Test
    void example2() { 
        int[][] matrix = { { 1, 3, 5, 7 }, { 10, 11, 16, 20 }, { 23, 30, 34, 60 } }; 
        boolean output = sol.searchMatrix(matrix, 13);
        assertFalse(output);
    };
}
