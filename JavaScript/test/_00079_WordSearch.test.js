const exist = require("../src/_00079_WordSearch");

test("Example 1", () => {
    const board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ];
    const word = "ABCCED";
    expect(exist(board, word)).toBe(true);
});

test("Example 2", () => {
    const board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ];
    const word = "SEE";
    expect(exist(board, word)).toBe(true);
});

test("Example 3", () => {
    const board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"],
    ];
    const word = "ABCB";
    expect(exist(board, word)).toBe(false);
});

test("Example 4", () => {
    const board = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"],
    ];
    const word = "ABCESEEEFS";
    expect(exist(board, word)).toBe(true);
});
