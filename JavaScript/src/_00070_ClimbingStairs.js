/**
 * Given `n` steps to reach the top of a staircase, find the number of distinct
 * ways you can climb to the top if each time you can either climb 1 or 2 steps.
 * @param {number} n number of steps
 * @returns {number} number of distinct ways to climb to the top of the stairs
 */
var climbStairs = function (n) {
    // If standing on any step `n`, one of two possibilities must have occured
    // in the last climb to get to this step. We were either on step `n - 1` and 
    // took one step, or we were on step `n - 2` and took two steps. The number
    // of ways to reach `n` is always the number of ways to reach `n - 1` and
    // the number of ways to reach `n - 2`.

    // Base case:
    // If there are 0 or 1 steps, there is exactly 1 way to reach the top.
    // (Either you're already there, or you take a single step.)
    if (n <= 1) return 1;

    // prev2 represents ways(i - 2)
    // Initially, ways(0) = 1
    let prev2 = 1; 

    // prev1 represents ways(i - 1)
    // Initially, ways(1) = 1
    let prev1 = 1;

    // Build the solution from step 2 up to step n
    for (let i = 2; i <= n; i++) {
        // The current number of ways is the sum of:
        // ways to reach previous step (i - 1)
        // plus ways to reach two steps before (i - 2)
        let current = prev1 + prev2;

        // Shift values forward for next iteration:
        // The old prev1 becomes prev2.
        prev2 = prev1;
        // The newly computed current becomes prev1.
        prev1 = current;
    }

    // After the loop, prev1 holds ways(n).
    return prev1;
}

/**
 * Given `n` steps to reach the top of a staircase, find the number of distinct
 * ways you can climb to the top if each time you can either climb 1 or 2 steps.
 * @param {number} n number of steps
 * @returns {number} number of distinct ways to climb to the top of the stairs
 */
var climbStairs1 = function (n) {
    // If standing on any step `n`, one of two possibilities must have occured
    // in the last climb to get to this step. We were either on step `n - 1` and 
    // took one step, or we were on step `n - 2` and took two steps. The number
    // of ways to reach `n` is always the number of ways to reach `n - 1` and
    // the number of ways to reach `n - 2`.
    if (n === 0 || n === 1) return 1;
    return climbStairs(n - 1) + climbStairs(n - 2);
};

module.exports = { climbStairs, climbStairs1 };
