const { canJump } = require("../src/_00055_JumpGame");

test("example1", () => {
    expect(canJump([2, 3, 1, 1, 4])).toBe(true);
});

test("example2", () => {
    expect(canJump([3, 2, 1, 0, 4])).toBe(false);
});

test("last number is irrelevant", () => {
    expect(canJump([3, 2, 1, 0])).toBe(true);
});

test("single value 0 should be false", () => {
    expect(canJump([0])).toBe(true);
})

test("first value 0 should be false", () => {
    expect(canJump([0, 5, 5])).toBe(false);
})
