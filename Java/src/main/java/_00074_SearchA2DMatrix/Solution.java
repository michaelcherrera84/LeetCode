package _00074_SearchA2DMatrix;

public class Solution {

    /**
     * You are given an {@code m x n} integer matrix {@code matrix} with the
     * following two properties:
     * <ul>
     * <li>Each row is sorted in non-decreasing order.</li>
     * <li>The first integer of each row is greater than the last integer of the
     * previous row.</li>
     * </ul>
     * Given an integer {@code target}, return {@code true} <i>if</i> {@code target}
     * <i>is in</i> {@code matrix} <i>or</i> {@code false} <i>otherwise</i>.
     * <p>
     * You must write a solution in {@code O(log(m * n))} time complexity.
     * 
     * @param matrix an {@code m x n} sorted integer matrix
     * @param target a value to find in the {@code matrix}
     * @return {@code true} if the value if found or {@code false} otherwise
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        // Treat the matrix like a 1D array to perform a binary search.
        int left = 0; // beginning of the matrix
        int right = rows * cols - 1; // end of the matrix

        // Check the middle of the array for the target, and "discard" half of 
        // the array if the target is not found. Continue until the value is 
        // found or there are no elements left.
        while (left <= right) {
            int mid = (left + right) / 2;

            int r = mid / cols;
            int c = mid % cols;

            if (matrix[r][c] == target)
                return true;
            else if (target < matrix[r][c])
                right = mid - 1;
            else
                left = mid + 1;
        }

        return false;
    }
}