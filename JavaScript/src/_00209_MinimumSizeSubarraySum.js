/**
 * Given an array of positive integers `nums` and a positive integer `target`,
 * return *the **minimal length** of a subarray whose sum is greater than or
 * equal to* `target`. If there is no such subarray, return `0` instead.
 * @param {number} target the sum to search for
 * @param {number[]} nums the array of positive integers
 * @return {number} the minimal length of a subarray whose sum is greater than
 * or equal to `target`
 */
var minSubArrayLen = function (target, nums) {
    const len = nums.length;
    let minLen = len + 1; // the minimal length of a subarray
    let sum = 0; // a running sum
    let left = 0;

    // For each element in the array, add the element to the running sum.
    for (let right = 0; right < len; right++) {
        sum += nums[right];

        // While the sum is greater than or equal to the target, shrink the
        // window by subtracting the first number from the sum and advancing
        // the left pointer.
        while (sum >= target) {
            minLen = Math.min(minLen, right - left + 1);
            sum -= nums[left];
            left += 1;
        }
    }

    // If minLen has not changed, no subarray was found.
    return minLen === len + 1 ? 0 : minLen;
};

module.exports = minSubArrayLen;
