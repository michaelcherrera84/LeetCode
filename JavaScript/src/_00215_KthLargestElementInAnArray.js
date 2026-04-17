/**
 * Given an integer array `nums` and an integer `k`, return the `kᵗʰ` *largest
 * element in the array*.
 *
 * Note that it is the `kᵗʰ` largest element in the sorted order, not the `kᵗʰ`
 * distinct element.
 *
 * Can you solve it without sorting?
 *
 * @param {number[]} nums list of integers
 * @param {number} k the element to find (kᵗʰ largest)
 * @return {number} the kᵗʰ largest element
 */
var findKthLargest = function (nums, k) {
    let left = 0;
    let right = nums.length;

    /**
     * Partition the array into parts:
     * 
     * ```text
     * nums[l ... <l>]     -> values > pivot
     * nums[<l> ... i-1]   -> values == pivot
     * nums[i ... r-1]     -> unknown
     * nums[r ... end]     -> values < pivot
     * ```
     * 
     * @param {number} l beginning of range
     * @param {number} r end of range
     * @param {number} p pivot index
     * @returns new pivot range
     */
    function partition(l, r, p) {
        const pivot = nums[p]; // element to partition the range around
        
        // Move the pivot to the beginning of the array.
        [nums[l], nums[p]] = [nums[p], nums[l]];

        let i = l + 1; // current element to compare to the pivot

        while (i < r) {
            if (nums[i] > pivot) {
                [nums[l], nums[i]] = [nums[i], nums[l]];
                l++;
                i++;
            } else if (nums[i] == pivot) i++;
            else {
                r--;
                [nums[i], nums[r]] = [nums[r], nums[i]];
            }
        }

        // Return the new pivot range (`i` not inclusive)
        return [l, i];
    }

    while (true) {
        const pivotIndex = Math.floor(Math.random() * (right - left) + left);
        const [low, high] = partition(left, right, pivotIndex);

        // k-th highest value is in the pivot region.
        if (low < k && k <= high) return nums[low];
        // k-th highest value is in the region greater than the pivot.
        else if (k <= low) right = low;
        // k-th highest value is in the region less than the pivot.
        else left = high;
    }
};

module.exports = findKthLargest;
