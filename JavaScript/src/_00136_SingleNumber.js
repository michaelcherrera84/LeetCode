/**
 * Given a **non-empty** array of integers `nums`, every element appears *twice*
 * except for one. Return that element.
 * @param {number[]} nums array of integers
 * @returns {number} the one element that doesn't appear twice
 */
var singleNumber = function (nums) {
    let num;  // to hold the number that appears only once

    // For each number in nums, XOR the number with num and store the result in
    // num. Duplicate numbers will cancel.
    for (let i = 0; i < nums.length; i++) {
        num = nums[i] ^ num;
    }

    return num;
};

module.exports = { singleNumber };
