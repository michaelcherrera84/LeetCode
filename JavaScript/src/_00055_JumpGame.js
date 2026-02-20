/**
 * Given an integer array `nums`, begin at the **first index**. Each element in
 * the array represents a maximum jump length at that position. Return `true`
 * *if you can reach the last index, or* `false` *otherwise*.
 * @param {number[]} nums array of numbers that represent maximum jump lengths
 * at each position
 * @returns {boolean} `true` if you can reach the last index, or `false`
 * otherwise
 */
var canJump = function (nums) {
    let farthest = 0;

    for (let i = 0; i < nums.length; i++) {
        // If we land on an index farther than the farthest,
        // there is no way to get here.
        if (i > farthest) return false;

        // If the jump lenght at this position would land us father than the 
        // farthest, then we have a new fathest.
        farthest = Math.max(farthest, i + nums[i]);

        // If at any point the farthest is the same or farther than the last
        // index, then we can reach the last index.
        if (farthest >= nums.length - 1) return true;
    }

    // This shouldn't happen.
    return false;
};

module.exports = { canJump };
