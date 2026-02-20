/**
 * Given an array of integers `nums`, start at index 0. Each element `nums[i]`
 * represents the maximum length of a forward jump from index `i`. Return *the
 * minimum number of jumps to reach index* `n - 1`.
 * @param {number[]} nums array of integers that each represent the maximum
 * length of a forward jump from that index
 * @returns {number} the minimum number of jumps to reach the last index
 */
var jump = function (nums) {
    // the farthest index we can reach from positions in the current range
    let farthest = 0;
    // the farthest index we can reach using current number of jumps
    let currEnd = 0;
    // number of committed jumps
    let jumps = 0;

    // Stop jumping at second to last index because we don't need to jump
    // anymore once we reach the last index.
    for (let i = 0; i < nums.length - 1; i++) {
        // While scanning the current range, compute the best possible reach
        // for the next jump.
        farthest = Math.max(farthest, i + nums[i]);

        // If we've reached the end of the current jump's range, we must make
        // another jump.
        if (i === currEnd) {
            jumps++;
            // The new range extends to the farthest we've found.
            currEnd = farthest; 
        }
    }

    return jumps;
};

module.exports = { jump };
