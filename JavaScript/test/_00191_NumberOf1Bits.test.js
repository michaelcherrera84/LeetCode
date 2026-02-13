const { hammingWeight } = require("../src/_00191_NumberOf1Bits");

test("example1", () => {
    expect(hammingWeight(11)).toBe(3);
});

test("example2", () => {
    expect(hammingWeight(128)).toBe(1);
});

test("example3", () => {
    expect(hammingWeight(2147483645)).toBe(30);
});

test("1 has 1 set bit", () => {
    expect(hammingWeight(1)).toBe(1);
});

test("2147483647 has 31 set bits", () => {
    expect(hammingWeight(2147483647)).toBe(31);
})