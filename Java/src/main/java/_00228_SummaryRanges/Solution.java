package _00228_SummaryRanges;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    /**
     * Given a <b>sorted unique</b> integer array {@code nums}, return <i>the
     * <b>smallest sorted</b> list of ranges that <b>cover all the numbers in
     * the array exactly</b></i>. That is, each element of {@code nums} is
     * covered by exactly one of the ranges, and there is no integer {@code x}
     * such that {@code x} is in one of the ranges but not in {@code nums}.
     * <p>
     * A <b>range</b> {@code [a,b]} is the set of all integers from {@code a} to
     * {@code b} (inclusive).
     * <p>
     * Each range {@code [a,b]} in the list should be formatted as follows:
     * <ul>
     * <li>{@code "a->b"} if {@code a != b}</li>
     * <li>{@code "a"} if {@code a == b}</li>
     * </ul>
     *
     * @param nums the sorted unique integer array
     * @return the smallest sorted {@linkplain List} of ranges that cover all
     * the numbers in the array exactly
     */
    public List<String> summaryRanges(int[] nums) {

        // ranges that cover all the numbers in the array exactly
        List<String> ranges = new ArrayList<>();
        if (nums.length == 0) {
            return ranges;
        }

        // The first number in the array is always the beginning of the first range.
        int start = nums[0];

        for (int i = 1; i <= nums.length; i++) {

            // If there is a current number, and the current number is not one 
            // greater than the previous number, then the current number is not 
            // part of the current range. The previous number is the end of the 
            // current range.
            if (i == nums.length || nums[i] != nums[i - 1] + 1) {

                // If the previous number is the same as the beginning of the 
                // current range, then add the number by itself as a range. 
                // Otherwise, build the range string in the form (first->last).
                if (nums[i - 1] == start) {
                    ranges.add(start + "");
                } else {
                    ranges.add(start + "->" + nums[i - 1]);
                }

                // Record the beginning of the next range.
                if (i < nums.length) {
                    start = nums[i];
                }
            }
        }

        return ranges;
    }
}
