class Solution:
    def longestPrefixSuffix(self, s: str) -> list[int]:
        """Construct an array where each index represents a position in a given
        string. Each element stores the length of a prefix that is also a suffix of
        the substring ending at that position.

        Args:
            s (str): the given string

        Returns:
            list[int]: an array of longest prefixes that are also suffixes of
            substrings that end at the corresponding index in `s`
        """

        lps = [0] * len(s)  # array of longest prefixes that are also suffixes

        i = 1  # the first 1-letter substring has no prefix/suffix
        j = 0  # current index in prefix
        while i < len(s):

            # If suffix letter is the same as the prefix letter, increment the prefix.
            # Then store the index value in the longest prefex suffix array, and
            # continue to the next letter of the current suffix.
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                # If the letters don't match, and if the prefix index is not 0, set
                # the prefix index to the previous match index. If the prefix index
                # is zero, this suffix doesn't match any prefix. Set the value of
                # lps to zero and advance to the next suffix.
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        """Given two strings `needle` and `haystack`, return the index of the 
        first occurrence of `needle` in `haystack`, of `-1` if `needle` is not
        part of `haystack`.

        Args:
            haystack (str): the string to search
            needle (str): the string to search for

        Returns:
            int: the fist index of `needle` in `haystack` of `-1` if `needle`
            is not in `haystack`
        """

        if len(haystack) == 0 or len(needle) == 0:
            return -1

        lcp = self.longestPrefixSuffix(needle)

        i = 0  # beginning of haystack
        j = 0  # beginning of needle
        while i < len(haystack):  # travers the string haystack

            # If the current letters of both strings match, advance to the next
            # letter of both strings.
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                # If we reach the end of needle, return the position in haystack
                # where needle begins.
                if j == len(needle):
                    return i - j
            else:
                # Otherwize, if not on the first letter of needle, refer to the lcp
                # array to see how far back in needle we can jump without missing
                # potential matches. If on the fist letter of needs, advance to the
                # next letter in haystack.
                if j != 0:
                    j = lcp[j - 1]
                else:
                    i += 1

        return -1

sol = Solution()
s = "abba"
sub = "ba"
print(sol.strStr(s, sub))
