const reverseWords = require("../src/_00151_ReverseWordsInAString");

test("Example 1", () => {
    expect(reverseWords("the sky is blue")).toBe("blue is sky the");
});

test("Example 2", () => {
    expect(reverseWords("  hello world  ")).toBe("world hello");
});

test("Example 3", () => {
    expect(reverseWords("a good   example")).toBe("example good a");
});

test("One word returns word", () => {
    expect(reverseWords("word")).toBe("word");
})
