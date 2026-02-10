const { searchInsert } = require("../src/_00035_SearchInsertPosition");

test("example1", () => {
    expect(searchInsert([1, 3, 5, 6], 5)).toBe(2);
});

test("example2", () => {
    expect(searchInsert([1, 3, 5, 6], 2)).toBe(1);
});

test("example3", () => {
    expect(searchInsert([1, 3, 5, 6], 7)).toBe(4);
});

test("array of length 1 target less", () => {
    expect(searchInsert([5], 3)).toBe(0);
});

test("array of lengh 1 target greater", () => {
    expect(searchInsert([5], 6)).toBe(1);
});
