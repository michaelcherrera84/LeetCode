const minSubArrayLen = require("../src/_00209_MinimumSizeSubarraySum");

test("Example 1", () => {
    const target = 7;
    const nums = [2, 3, 1, 2, 4, 3];
    const expected = 2;
    const actual = minSubArrayLen(target, nums);
    expect(actual).toBe(expected);
});

test("Example 2", () => {
    const target = 4;
    const nums = [1, 4, 4];
    const expected = 1;
    const actual = minSubArrayLen(target, nums);
    expect(actual).toBe(expected);
});

test("Example 3", () => {
    const target = 11;
    const nums = [1, 1, 1, 1, 1, 1, 1, 1];
    const expected = 0;
    const actual = minSubArrayLen(target, nums);
    expect(actual).toBe(expected);
});
