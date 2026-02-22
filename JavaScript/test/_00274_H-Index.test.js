const { hIndex } = require("../src/_00274_H-Index");

test("example1", () => {
    expect(hIndex([3, 0, 6, 1, 5])).toBe(3);
});

test("example2", () => {
    expect(hIndex([1, 3, 1])).toBe(1);
});

test("1 paper with 0 citations has 0 h-index", () => {
    expect(hIndex([0])).toBe(0);
})