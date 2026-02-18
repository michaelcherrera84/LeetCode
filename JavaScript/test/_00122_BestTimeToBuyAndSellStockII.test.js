const { maxProfit } = require("../src/_00122_BestTimeToBuyAndSellStockII");

test("example1", () => {
    expect(maxProfit([7, 1, 5, 3, 6, 4], 7)).toBe(7);
});

test("example2", () => {
    expect(maxProfit([1, 2, 3, 4, 5], 5)).toBe(4);
});

test("example3", () => {
    expect(maxProfit([7, 6, 4, 3, 1], 0)).toBe(0);
});
