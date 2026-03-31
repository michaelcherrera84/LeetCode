#include <gtest/gtest.h>
#include "../src/_00208_ImplementTrie.cpp"

TEST(ImplementTrie, Example1)
{
    Trie trie = Trie();
    trie.insert("apple");
    EXPECT_TRUE(trie.search("apple"));
    EXPECT_FALSE(trie.search("app"));
    EXPECT_TRUE(trie.startsWith("app"));
    trie.insert("app");
    EXPECT_TRUE(trie.search("app"));
}