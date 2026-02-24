#include <string>
#include <algorithm>

class Solution
{
public:
    /// @brief Given an input string `s`, reverse the order of the **words**.
    /// 
    /// A **word** is definied as a sequence of non-space characters. The
    /// **words** in `s` will be separated by at least one space.
    ///
    /// Return *a string of the words in reverse order concatenated by a single
    /// space*.
    /// @param s the input string
    /// @return the string of words in reverse order concatenated by a single 
    /// space
    std::string reverseWords(std::string s)
    {
        // Trim unwanted spaces.
        trim(s);
        // Reverse the entire string.
        reverse(s, 0, s.length() - 1);

        // Now the words are in the correct order, but they are backwards, so we
        // reverse each word indivdiually.
        int i = 0;
        while (i < s.length())
        {
            int start = i; // the beginning of a word
            // Find the end of a word.
            while (i < s.length() && s[i] != ' ')
                i++;
            // Reverse the word.
            reverse(s, start, i - 1);
            i++;
        }

        return s;
    }

private:
    /**
     * Remove leading spaces, trailing spaces, and internal consecutive spaces
     * from a string.
     * @param s the string
     */
    void trim(std::string &s)
    {
        int n = s.length();
        int read = 0;  // current read position
        int write = 0; // current write position

        // Skip leading spaces.
        while (read < n && s[read] == ' ')
            read++;

        while (read < n)
        {
            // Copy characters from the read position to the write position.
            while (read < n && s[read] != ' ')
                s[write++] = s[read++];

            // Skip spaces between words.
            while (read < n && s[read] == ' ')
                read++;

            // Add single space if not at the end of the string.
            if (read < n)
                s[write++] = ' ';
        }

        // Remove the left over spaces after trimming the string.
        s.resize(write);
    }

    /**
     * Reverse the characters of a string from the a starting position to an
     * ending position
     * @param s the string
     * @param begin the starting position
     * @param end the ending position
     */
    void reverse(std::string &s, int begin, int end)
    {
        while (begin < end)
        {
            std::swap(s[begin++], s[end--]);
        }
    }
};