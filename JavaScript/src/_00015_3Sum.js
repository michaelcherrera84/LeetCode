/**
 * Given an integer array nums, return all the triplets
 * `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and
 * `nums[i] + nums[j] + nums[k] == 0`, without duplicate triplets.
 * @param {number[]} nums the integer array
 * @return {number[][]} the array of triplets that sum to zero
 */
var threeSum = function (nums) {
    nums = nums.sort((a, b) => a - b);

    const res = [];
    const len = nums.length;

    // For each number in nums, search for two other numbers that when added to
    // the current number will equal zero.
    for (let i = 0; i < len - 2; i++) {
        // Skip duplicate numbers.
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = len - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];

            // If sum is greater than zero, the right value is too high.
            if (sum > 0) right--;
            // if the sum is less than zero, the left value is too low.
            else if (sum < 0) left++;
            // Otherwise, we have found a triplet.
            else {
                res.push([nums[i], nums[left], nums[right]]);
                left++;
                right--;

                // Skip duplicate left values and right values.
                while (left < right && nums[left] === nums[left - 1]) left++;
                while (left < right && nums[right] === nums[right + 1]) right--;
            }
        }
    }

    return res;
};

module.exports = threeSum;
