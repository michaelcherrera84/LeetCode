const { isPalindrome } = require("../src/_00009_PalindromeNumber");

test("example1", () => {
    expect(isPalindrome(121)).toBe(true);
});

test("example2", () => {
    expect(isPalindrome(-121)).toBe(false);
});

test("example3", () => {
    expect(isPalindrome(10)).toBe(false);
});

test("2^31 - 1 is not palindrome", () => {
    expect(isPalindrome(2_147_483_647)).toBe(false);
});

test("-2^31 is not palindrome", () => {
    expect(isPalindrome(-2_147_483_648)).toBe(false);
})

test("1234564321 is not a palindrome", () => {
    expect(isPalindrome(1_234_564_321)).toBe(false);
})

test("1234554321 is a palindrome", () => {
    expect(isPalindrome(1_234_554_321)).toBe(true);
})

test("12345654321 is a palindrome", () => {
    expect(isPalindrome(12_345_654_321)).toBe(true);
})