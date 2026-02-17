/**
 * Given an integer array `nums`, rotate the array to the right by `k` steps,
 * where `k` is non-negative.
 * @param {number[]} nums integer array
 * @param {number} k steps to rotate the array to the right
 */
var rotate = function (nums, k) {
    const n = nums.length;
    // k can be longer than the length of the array, and potentially result in
    // many full rotations.
    k = k % n;

    /**
     * Reverse an array or portion of an array.
     * @param {number} start beginning of sub-array
     * @param {number} end end of sub-array
     */
    const reverse = (start, end) => {
        // If start is less than end, there are still elements to swap.
        while (start < end) {
            // Swap the start and end elements.
            [nums[start], nums[end]] = [nums[end], nums[start]];
            start++;
            end--;
        }
    };

    reverse(0, n - 1);  // Reverse the entire array.
    reverse(0, k - 1);  // Reverse the part of the array before the number of steps.
    reverse(k, n - 1);  // Reverse the part of the array from the number of steps on.
};

module.exports = { rotate };
