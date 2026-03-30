const { snakesAndLadders } = require("../src/_00909_SnakesAndLadders");

test("Example 1", () => {
    const board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ];
    const expected = 4;
    const actual = snakesAndLadders(board);
    expect(actual).toBe(expected);
});

test("Example 2", () => {
    const board = [
        [-1, -1],
        [-1, 3],
    ];
    const expected = 1;
    const actual = snakesAndLadders(board);
    expect(actual).toBe(expected);
});
