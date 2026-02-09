import Cocoa

class Solution {

    /// Construct an array where each index represents a postion in a given string. Each element stores the
    /// length of a prefix that is also a suffix of the substring ending at that position.
    /// - Parameter s: the given string
    /// - Returns: an array of longest prefix/suffix of substrings ending at each
    /// position
    func longestPrefixSuffix(_ s: String) -> [Int] {

        // array of longest prefixes that are also suffixes
        var lps = Array(repeating: 0, count: s.count)
        let arrayS = Array(s)

        var i = 1  // the first prefix/suffix is always 0
        var len = 0  // the length of a prefix/suffix

        while i < s.count {

            // If the letters at i and len match, they are part of a prefix/suffix.
            // We can increase the lenght of the prefix/suffix and store the value
            // for this position in the array.
            if arrayS[i] == arrayS[len]
            {
                len += 1
                lps[i] = len
                i += 1
            } else {  // If the letters at i an len do not match...

                // If the len value is not 0, we shrink length to the previous
                // length and check the current position again for a shorter
                // prefix/suffix
                if len != 0 {
                    len = lps[len - 1]
                } else {  // Otherse, there is not suffix/prefix for this position.
                    lps[i] = 0
                    i += 1
                }
            }
        }

        return lps
    }


    /// Given two strings `needle` and `haystack`, return the index of the first occurence of `needle`
    /// in `haystack`, or `-1` if `needle` is not part of `haystack`.
    /// - Parameters:
    ///   - haystack: the string to search
    ///   - needle: the string to search for
    /// - Returns: the first index of `needle` in `haystack` or `-1` if `needle` is not in `paycheck`
    func strStr(_ haystack: String, _ needle: String) -> Int {

        if needle.isEmpty || haystack.isEmpty {
            return -1
        }

        let hArray = Array(haystack)
        let nArray = Array(needle)

        let lps = longestPrefixSuffix(needle)  // longest prefix/suffix array

        var i = 0
        var j = 0
        while i < hArray.count {
            // If the current letters in needle and haystack match, advance
            // to the next letters.
            if hArray[i] == nArray[j]
            {
                i += 1
                j += 1

                // If the needle pointer has reached the end of needle, an
                // index of needle has been found. Return the index for the
                // first letter in needle.
                if j == nArray.count {
                    return i - j
                }
            } else {  // If the letter do not match...

                // If not on the first letter of needle, check the
                // prefix/suffix array for the needle index we can return to
                // without missing any potential matches.
                if j != 0 {
                    j = lps[j - 1]
                } else {
                    // If already on the first letter of needs, advance to
                    // the next letter in haystack.
                    i += 1
                }
            }
        }

        return -1
    }
}

let sol = Solution()
sol.strStr("abababcdabab", "abc")
