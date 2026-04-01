/**
 * Given a string containing digits from `2-9` inclusive, return all possible
 * letter combinations that the number could represent. Return the answer in
 * `any order`.
 *
 * A mapping of digits to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 * ```txt
 * 1        2 abc    3 def
 * 4 ghi    5 jkl    6 mno
 * 7 pqrs   8 tuv    9 wxyz
 *          0  ␣
 * ```
 * @param {string} digits the digits to find combinations for
 * @return {string[]} all possible letter combinations for the `digits`
 */
var letterCombinations = function (digits) {
    if (!digits) return [];

    /** Mapping of digits to corresponding letters. */
    const mapping = {
        0: " ",
        1: "",
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    };

    const combos = [];

    /**
     * Recursively build letter combinations represented by the digits.
     * @param {number} i index of current digit
     * @param {string} combo current letter combination
     */
    function findCombos(i, combo) {
        // Each time we add a letter from the final digit, add the combo to the
        // result list and return to the previous digit.
        if (i === digits.length) {
            combos.push(combo);
            return;
        }

        for (c of mapping[digits[i]]) {
            findCombos(i + 1, combo + c);
        }
    }

    findCombos(0, "");

    return combos;
};

module.exports = letterCombinations;
