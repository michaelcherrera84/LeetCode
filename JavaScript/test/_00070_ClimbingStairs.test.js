const { climbStairs, climbStairs1 } = require("../src/_00070_ClimbingStairs");

test("example1", () => {
    expect(climbStairs(2)).toBe(2);
});

test("example2", () => {
    expect(climbStairs(3)).toBe(3);
});

test("45 steps has 1836311903 distinct ways to climb", () => {
    expect(climbStairs(45)).toBe(1836311903);
});

test("example1-1", () => {
    expect(climbStairs1(2)).toBe(2);
});

test("example2-1", () => {
    expect(climbStairs1(3)).toBe(3);
});

test("45 steps has 1836311903 distinct ways to climb-1", () => {
    expect(climbStairs1(45)).toBe(1836311903);
});
