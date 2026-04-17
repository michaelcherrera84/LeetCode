const findKthLargest = require("../src/_00215_KthLargestElementInAnArray");

test("Example 1", () => {
    const nums = [3, 2, 1, 5, 6, 4];
    const k = 2;
    const expected = 5;
    const actual = findKthLargest(nums, k);
    expect(actual).toBe(expected);
});

test("Example 2", () => {
    const nums = [3, 2, 3, 1, 2, 4, 5, 5, 6];
    const k = 4;
    const expected = 4;
    const actual = findKthLargest(nums, k);
    expect(actual).toBe(expected);
});
