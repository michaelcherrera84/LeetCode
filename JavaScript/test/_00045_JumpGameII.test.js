const { jump } = require("../src/_00045_JumpGameII");

test("example1", () => {
    expect(jump([2, 3, 1, 1, 4])).toBe(2);
});

test("example2", () => {
    expect(jump([2, 3, 0, 1, 4])).toBe(2);
});

test("reach the end in 1 jump", () => {
    expect(jump([2, 0, 1])).toBe(1);
});
