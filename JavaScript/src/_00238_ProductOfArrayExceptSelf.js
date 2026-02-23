/**
 * Given an integer array `nums`, return *an array* `answer` *such that*
 * `answer[i]` *is equal to the product of all the elements of* `nums` *except*
 * `nums[i]`.
 * @param {number[]} nums the integer array
 * @return {number[]} array whose elements are the product of elements of `nums`
 */
var productExceptSelf = function (nums) {
    const n = nums.length;
    const answer = new Array(nums.length);

    // --- PREFIX PASS ---
    // We build products of everything to the LEFT of each index.
    // For index 0, there is nothing to the left,
    // so the product is the multiplicative identity: 1.
    answer[0] = 1;
    for (let i = 1; i < n; i++) {
        // answer[i - 1] already contains the product of everything
        // to the left of (i - 1).
        //
        // Multiply that by nums[i - 1] to extend the prefix by one element.
        //
        // So answer[i] becomes:
        // product of nums[0] through nums[i - 1]
        answer[i] = answer[i - 1] * nums[i - 1];
    }

    // --- SUFFIX PASS ---
    // Now we multiply in products of everything to the RIGHT.
    // We'll walk backwards and maintain a running suffix product.
    //
    // Start with 1 because there is nothing to the right of
    // the last element.
    let suffix = 1;
    for (let i = n - 1; i >= 0; i--) {
        // answer[i] currently holds:
        // product of everything to the LEFT of i
        //
        // suffix holds:
        // product of everything to the RIGHT of i
        //
        // Multiply them together to get:
        // product of everything except nums[i]
        answer[i] *= suffix;

        // Multiplying a negative number by 0 can produce -0, so set to 0.
        if (answer[i] === 0) answer[i] = 0;

        // Now extend the suffix for the next iteration (moving left).
        // After this, suffix becomes:
        // product of nums[i] through nums[n - 1]
        suffix *= nums[i];
    }

    return answer;
};

module.exports = { productExceptSelf };
