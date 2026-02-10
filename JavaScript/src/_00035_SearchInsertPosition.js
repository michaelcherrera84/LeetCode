/**
 * Given a sorted array of distinct integers and a target value, return the
 * index if the target is found. If not, return the index where it would be if
 * it were inserted in order.
 * @param {number} nums sorted array of distinct integers
 * @param {number} target target value
 * @returns {number} index of the target if found, or the index where it would
 * be inserted
 */
var searchInsert = function (nums, target) {
    /**
     * Since the array is sorted, we can cut the array or sub-array in half each
     * iteration and disregard that half that cannot contain the target.
     * @param {number} left pointer to lowest value of sub-array
     * @param {number} right pointer to highest value of sub-array
     * @returns index of target or index where target belongs
     */
    const search = (left, right) => {
        // If left is greater than right, there are no more elements to search 
        // and left is the position where the target belongs.
        if (left > right) return left;

        const mid = (left + right) >> 1;    // middle element of the array

        if (nums[mid] === target) {
            // If we mid is the target return the index mid.
            return mid;
        } else if (nums[mid] < target) {
            // Otherwise, continue the search with the right half of the sub-array.
            return search(mid + 1, right);
        } else {
            // Otherwise, continue the search with the left half of the sub-array.
            return search(left, mid - 1);
        }
    };

    return search(0, nums.length - 1);
};

module.exports = { searchInsert };
