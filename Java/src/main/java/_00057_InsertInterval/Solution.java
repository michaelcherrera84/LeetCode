package _00057_InsertInterval;

public class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) return new int[][] {newInterval};

        // 1. Binary search for the 'left' index
        // Finding the first interval where interval[1] >= newInterval[0]
        int left = 0, right = intervals.length - 1;
        int start = intervals.length; 
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (intervals[mid][1] >= newInterval[0]) {
                start = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // 2. Binary search for the 'right' index
        // Finding the first interval where interval[0] > newInterval[1]
        left = start; // Optimization: We only need to search from start onwards
        right = intervals.length - 1;
        int end = intervals.length;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (intervals[mid][0] > newInterval[1]) {
                end = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        // 3. Merge the overlapping intervals into newInterval (if overlaps exist)
        if (start < end) {
            newInterval[0] = Math.min(newInterval[0], intervals[start][0]);
            newInterval[1] = Math.max(newInterval[1], intervals[end - 1][1]);
        }

        // 4. Construct the final array.
        int[][] result = new int[start + 1 + (intervals.length - end)][];
        
        // Copy the strictly left intervals
        System.arraycopy(intervals, 0, result, 0, start);
        
        // Insert the merged newInterval
        result[start] = newInterval;
        
        // Copy the strictly right intervals
        System.arraycopy(intervals, end, result, start + 1, intervals.length - end);

        return result;
    }
}