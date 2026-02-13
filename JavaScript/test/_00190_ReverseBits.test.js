const { reverseBits } = require("../src/_00190_ReverseBits");

test("example1", () => {
    expect(reverseBits(43261596)).toBe(964176192);
});

test("example2", () => {
    expect(reverseBits(2147483644)).toBe(1073741822);
});

test("0 reversed is 0", () => {
    expect(reverseBits(0)).toBe(0);
});

test("2^31 - 1 reversed is", () => {
    expect(reverseBits(2147483646)).toBe(2147483646)
})
