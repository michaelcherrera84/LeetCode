package _00215_KthLargestElementInAnArray;

public class Solution {

    /**
     * Given an integer array {@code nums} and an integer {@code k}, return
     * <i>the</i> {@code kᵗʰ} <i>largest element in the array</i>.
     * <p>
     * Note that it is the {@code kᵗʰ} largest element in the sorted order, not the
     * {@code kᵗʰ} distinct element.
     * <p>
     * Can you solve it without sorting?
     * 
     * @param nums array of integers
     * @param k    element to find (kᵗʰ largest)
     * @return the kᵗʰ largest element
     */
    public int findKthLargest(int[] nums, int k) {
        int left = 0;
        int right = nums.length;

        while (true) {
            int pivotIndex = (int) (Math.random() * (right - left) + left);

            int[] pivotRange = partition(left, right, pivotIndex, nums);

            if (pivotRange[0] < k && k <= pivotRange[1])
                return nums[pivotRange[0]];
            else if (k <= pivotRange[0])
                right = pivotRange[0];
            else
                left = pivotRange[1];
        }
    }

    /**
     * Partially sort a range of an array around a pivot.
     * 
     * @param l    beginning of range
     * @param r    end of range
     * @param p    pivot index
     * @param nums an array of integers
     * @return the pivot range ({@code i} not inclusive)
     */
    private int[] partition(int l, int r, int p, int[] nums) {
        int pivot = nums[p];
        swap(l, p, nums); // Move the pivot to the beginning of the array.
        int i = l + 1; // current element to compare to the pivot

        while (i < r) {
            if (nums[i] > pivot) {
                swap(l, i, nums);
                l++;
                i++;
            } else if (nums[i] == pivot)
                i++;
            else {
                r--;
                swap(i, r, nums);
            }
        }

        return new int[] { l, i };
    }

    /**
     * Swap two elements in an array.
     * 
     * @param i   an element index
     * @param j   an element index
     * @param arr an array with elements to swap
     */
    private void swap(int i, int j, int[] arr) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}