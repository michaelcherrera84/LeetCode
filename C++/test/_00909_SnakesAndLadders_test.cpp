#include <gtest/gtest.h>
#include "../src/_00909_SnakesAndLadders.cpp"

TEST(SnakesAndLadders, Example1)
{
    Solution sol;

    std::vector<std::vector<int>> board = {
        {-1, -1, -1, -1, -1, -1}, 
        {-1, -1, -1, -1, -1, -1}, 
        {-1, -1, -1, -1, -1, -1}, 
        {-1, 35, -1, -1, 13, -1}, 
        {-1, -1, -1, -1, -1, -1}, 
        {-1, 15, -1, -1, -1, -1}
    };
    int expected = 4;
    int actual = sol.snakesAndLadders(board);

    EXPECT_EQ(expected, actual);
}