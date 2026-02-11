const { addBinary, addBinary1 } = require("../src/_00067_AddBinary");

test("example1", () => {
    expect(addBinary("11", "1")).toBe("100");
});

test("example2", () => {
    expect(addBinary("1010", "1011")).toBe("10101");
});

test("example1-1", () => {
    expect(addBinary1("11", "1")).toBe("100");
});

test("example2-1", () => {
    expect(addBinary1("1010", "1011")).toBe("10101");
});

test("very large numbers", () => {
    let a = Math.floor(Math.random() * 5_000_000_000_000 + 5_000_000_000_000);
    let b = Math.floor(Math.random() * 5_000_000_000_000 + 5_000_000_000_000);
    let sum = (a + b).toString(2);
    console.log(sum);

    expect(addBinary(a.toString(2), b.toString(2))).toBe(sum);
});

test("very large numbers-1", () => {
    let a = Math.floor(Math.random() * 5_000_000_000_000 + 5_000_000_000_000);
    let b = Math.floor(Math.random() * 5_000_000_000_000 + 5_000_000_000_000);
    let sum = (a + b).toString(2);
    console.log(sum);

    expect(addBinary1(a.toString(2), b.toString(2))).toBe(sum);
});
