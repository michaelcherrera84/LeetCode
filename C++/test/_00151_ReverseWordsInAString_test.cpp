#include <gtest/gtest.h>
#include "../src/_00151_ReverseWordsInAString.cpp"

TEST(ReverseWordsInAString, Example1) {
    Solution sol;

    std::string input = "the sky is blue";
    std::string expected = "blue is sky the";

    EXPECT_EQ(sol.reverseWords(input), expected);
}

TEST(ReverseWordsInAString, Example2) {
    Solution sol;

    std::string input = "  hello world ";
    std::string expected = "world hello";

    EXPECT_EQ(sol.reverseWords(input), expected);
}

TEST(ReverseWordsInAString, Example3) {
    Solution sol;

    std::string input = "a good   example";
    std::string expected = "example good a";

    EXPECT_EQ(sol.reverseWords(input), expected);
}