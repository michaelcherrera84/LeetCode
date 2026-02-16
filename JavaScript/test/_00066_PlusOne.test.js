const { plusOne } = require("../src/_00066_PlusOne");

test("example1", () => {
    expect(plusOne([1, 2, 3])).toEqual([1, 2, 4]);
});

test("example2", () => {
    expect(plusOne([4, 3, 2, 1])).toEqual([4, 3, 2, 2]);
});

test("example3", () => {
    expect(plusOne([9])).toEqual([1, 0]);
});

test("[9, 9, 9] + 1 = [1, 0, 0, 0]", () => {
    expect(plusOne([9, 9, 9])).toEqual([1, 0, 0, 0]);
});

test("[8, 9, 9] + 1 = [9, 0, 0]", () => {
    expect(plusOne([8, 9, 9])).toEqual([9, 0, 0]);
});
