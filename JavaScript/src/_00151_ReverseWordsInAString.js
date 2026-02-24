/**
 * Given an input string `s`, reverse the order of the **words**.
 *
 * A **word** is definied as a sequence of non-space characters. The **words**
 * in `s` will be separated by at least one space.
 *
 * Return *a string of the words in reverse order concatenated by a single
 * space*.
 *
 * **Note** that `s` may contain leading or trailing spaces or multiple spaces
 * between two words. The returned string should only have a single space
 * separating the words. Do not include any extra spaces.
 * @param {string} s the input string
 * @return {string} the string of words in reverse order concatenated by a
 * single space
 */
var reverseWords1 = function (s) {
    let result = ""; // the words in reverse order
    let trimmed = s.trim(); // the string with no leading and trailing spaces
    let next = 0; // the start of the next word

    // For each character in the trimmed string, beginning with the last...
    for (let i = trimmed.length - 1; i >= 0; i--) {
        let char = trimmed[i]; // current character

        // If the character is not a space...
        if (char !== " ") {
            // place the character at the start of the next word.
            result = result.slice(0, next) + char + result.slice(next);
        } else {
            // If the chracter is a space...
            // and the end of the string is not a space...
            if (result[result.length - 1] !== " ") {
                result += char; // add the space to the end of the string.
                // Then end of the string will be the start of the next word.
                next = result.length;
            }
        }
    }

    return result;
};

/**
 * Given an input string `s`, reverse the order of the **words**.
 *
 * A **word** is definied as a sequence of non-space characters. The **words**
 * in `s` will be separated by at least one space.
 *
 * Return *a string of the words in reverse order concatenated by a single
 * space*.
 *
 * **Note** that `s` may contain leading or trailing spaces or multiple spaces
 * between two words. The returned string should only have a single space
 * separating the words. Do not include any extra spaces.
 * @param {string} s the input string
 * @return {string} the string of words in reverse order concatenated by a
 * single space
 */
var reverseWords2 = function (s) {
    const result = []; // array of the words in reverse order
    let i = s.length - 1;

    while (i >= 0) {
        // Find the end of a word.
        while (i >= 0 && s[i] === " ") i--;
        // If `i` is less than zero, we've reached the beginning of the string.
        if (i < 0) break;

        let end = i; // the end of the current word

        // Find the start of the current word.
        while (i >= 0 && s[i] !== " ") i--;

        // Add the current word to the result array
        result.push(s.slice(i + 1, end + 1));
    }

    // Join the words separated by a space.
    return result.join(" ");
};

/**
 * Given an input string `s`, reverse the order of the **words**.
 *
 * A **word** is definied as a sequence of non-space characters. The **words**
 * in `s` will be separated by at least one space.
 *
 * Return *a string of the words in reverse order concatenated by a single
 * space*.
 *
 * **Note** that `s` may contain leading or trailing spaces or multiple spaces
 * between two words. The returned string should only have a single space
 * separating the words. Do not include any extra spaces.
 * @param {string} s the input string
 * @return {string} the string of words in reverse order concatenated by a
 * single space
 */
var reverseWords = function (s) {
    return s.trim().split(/\s+/).reverse().join(" ");
};

module.exports = reverseWords;
