const { mySqrt, mySqrt1 } = require("../src/_00069_Sqrt_x_");

test("example1", () => {
    expect(mySqrt(4)).toBe(2);
});

test("example2", () => {
    expect(mySqrt(8)).toBe(2);
});

test("Sqrt of 0 is 0", () => {
    expect(mySqrt(0)).toBe(0);
});

test("Sqrt of 2147483647 is 46340", () => {
    expect(mySqrt(2147483647)).toBe(46340);
});


test("example1-1", () => {
    expect(mySqrt1(4)).toBe(2);
});

test("example2-1", () => {
    expect(mySqrt1(8)).toBe(2);
});

test("Sqrt of 0 is 0-1", () => {
    expect(mySqrt1(0)).toBe(0);
});

test("Sqrt of 2147483647 is 46340-1", () => {
    expect(mySqrt1(2147483647)).toBe(46340);
});
