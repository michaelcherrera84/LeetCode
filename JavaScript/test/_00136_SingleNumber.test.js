const { singleNumber } = require("../src/_00136_SingleNumber");

test("example1", () => {
    const nums = [2, 2, 1];
    expect(singleNumber(nums)).toBe(1);
});

test("example2", () => {
    const nums = [4,1,2,1,2];
    expect(singleNumber(nums)).toBe(4);
});

test("example3", () => {
    const nums = [1];
    expect(singleNumber(nums)).toBe(1);
});