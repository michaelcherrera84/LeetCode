const { rotate } = require("../src/_00189_RotateArray");

test("example1", () => {
    const nums = [1, 2, 3, 4, 5, 6, 7];
    rotate(nums, 3);
    expect(nums).toEqual([5, 6, 7, 1, 2, 3, 4]);
});

test("example1", () => {
    const nums = [-1, -100, 3, 99];
    rotate(nums, 2);
    expect(nums).toEqual([3, 99, -1, -100]);
});

test("[1,2,3,4,5,6] shifted 2 times should be [5,6,1,2,3,4]", () => {
    const nums = [1, 2, 3, 4, 5, 6];
    rotate(nums, 4);
    expect(nums).toEqual([3, 4, 5, 6, 1, 2]);
});

test("[1,2,3,4,5] shifted 100 times should be [1,2,3,4,5]", () => {
    const nums = [1, 2, 3, 4, 5];
    rotate(nums, 100);
    expect(nums).toEqual([1, 2, 3, 4, 5]);
});
