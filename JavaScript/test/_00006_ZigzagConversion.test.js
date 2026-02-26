const convert = require("../src/_00006_ZigzagConversion");

test("Example 1", () => {
    expect(convert("PAYPALISHIRING", 3)).toBe("PAHNAPLSIIGYIR");
});

test("Example 2", () => {
    expect(convert("PAYPALISHIRING", 4)).toBe("PINALSIGYAHRPI");
});
