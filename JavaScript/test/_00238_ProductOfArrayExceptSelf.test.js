const { productExceptSelf } = require("../src/_00238_ProductOfArrayExceptSelf");

const normalize = (arr) => arr.map((n) => (Object.is(n, -0) ? 0 : n));

test("example1", () => {
    const nums = [1, 2, 3, 4];
    const answer = productExceptSelf(nums);
    const expected = [24, 12, 8, 6];

    expect(normalize(answer)).toEqual(expected);
});

test("example2", () => {
    const nums = [-1, 1, 0, -3, 3];
    const answer = productExceptSelf(nums);
    const expected = [0, 0, 9, 0, 0];

    expect(normalize(answer)).toEqual(expected);
});
