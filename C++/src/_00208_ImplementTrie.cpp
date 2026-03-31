#include <string>
#include <map>

/**
 * A trie (pronounced as "try") or prefix tree is a tree data structure used
 * to efficiently store and retrieve keys in a dataset of strings. There are
 * various applications of this data structure, such as autocomplete and
 * spellchecker.
 */
class Trie
{
private:
    /**
     * Represents a character.
     */
    struct TrieNode
    {
        /** Characters that come immidiately after this character. */
        TrieNode *children[26]{nullptr};
        /** `true` if this character is the end of a word. */
        bool isEndOfWord = false;

        ~TrieNode()
        {
            for (int i = 0; i < 26; ++i)
            {
                delete children[i];
            }
        }
    };

    TrieNode *root;

public:
    /**
     * Initialize the trie object.
     */
    Trie()
    {
        root = new TrieNode();
    }

    ~Trie()
    {
        delete root;
    }

    /**
     * Insert the string `word` into the trie.
     * @param word the string to insert
     */
    void insert(std::string word)
    {
        TrieNode *curr = root;
        for (char c : word)
        {
            if (!curr->children[c - 'a'])
                curr->children[c - 'a'] = new TrieNode();
            curr = curr->children[c - 'a'];
        }
        curr->isEndOfWord = true;
    }

    /**
     * Return `true` if the string `word` is in the trie (i.e., was inserted
     * before), and `false` otherwise.
     * @param word the string to search for
     * @return `true` if the word is found or `false` otherwise
     */
    bool search(std::string word)
    {
        TrieNode *curr = root;

        for (char c : word)
        {
            if (!curr->children[c - 'a'])
                return false;
            curr = curr->children[c - 'a'];
        }

        return curr->isEndOfWord;
    }

    /**
     * Return `true` if there is a previously inserted string `word` that has
     * the prefix `prefix`, and `false` otherwise.
     * @param word the prefix to search for
     * @return `true` if a word has the `prefix` or `false` otherwise
     */
    bool startsWith(std::string prefix)
    {
        TrieNode *curr = root;

        for (char c : prefix)
        {
            if (!curr->children[c - 'a'])
                return false;
            curr = curr->children[c - 'a'];
        }

        return true;
    }
};