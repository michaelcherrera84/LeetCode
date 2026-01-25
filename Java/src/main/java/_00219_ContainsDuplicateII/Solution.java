package _00219_ContainsDuplicateII;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    /**
     * Given an integer array {@code nums} and an integer {@code k}, return
     * {@code true} <i>if there are two <b>distinct indices</b></i> {@code i}
     * <i>and</i> {@code j} <i>in the array such that</i>
     * {@code nums[i] == nums[j]} <i>and</i> {@code abs(i-j) <= k}.
     *
     * @param nums the integer array
     * @param k the integer
     * @return {@code true} if there are two indices in {@code nums} that
     * contain equal values are not more than {@code k} apart, or {@code false}
     * otherwise.
     */
    public boolean containsNearbyDuplicate(int[] nums, int k) {

        if (nums == null || nums.length < 1) {
            return false;
        }

        // to hold values and their indices
        Map<Integer, Integer> numAndIndex = new HashMap<>();

        // Traverse the array, tracking the most recent index of each value.
        for (int i = 0; i < nums.length; i++) {

            // If the current value has been seen and the absolute difference 
            // between the index of that value and the current index is less 
            // than or equal to k, a nearby duplicate has been found.
            if (numAndIndex.containsKey(nums[i]) && i - numAndIndex.get(nums[i]) <= k) {
                return true;
            }

            // Otherwise, store the value and its index.
            numAndIndex.put(nums[i], i);
        }

        // If the loop completes without returning true, no nearby duplicates were found.
        return false;
    }
}
