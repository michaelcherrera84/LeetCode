const letterCombinations = require("../src/_00017_LetterCombinationsOfAPhoneNumber");

test("Example 1", () => {
    const digits = "23";
    const expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"];
    const actual = letterCombinations(digits);
    expect(actual).toEqual(expect.arrayContaining(expected));
    expect(actual.length).toEqual(expected.length);
});

test("Example 2", () => {
    const digits = "2";
    const expected = ["a", "b", "c"];
    const actual = letterCombinations(digits);
    expect(actual).toEqual(expect.arrayContaining(expected));
    expect(actual.length).toEqual(expected.length);
});