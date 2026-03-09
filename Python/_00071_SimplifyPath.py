from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        """You are given an *absolute* path for a Unix-style file system, which
        always begins with a slash `/`. Your task is to transform this absolute
        path into its **simplified canonical path.**

        The *rules* of a Unix-style file system are as follows:
        - A single period `'.'` represents the current director.
        - A double period `'..'` represents the previous/parent directory.
        - Multiple consecutive slashes such as `'//'` and `'///'` are treated as
        a single slash `'/'`.
        - Any sequence of periods that does **not match** the rules above should
        be treated as a **valid directory or file name**. For example, `'...'`
        and `'....'` are valid directory or file names.

        The simplified canonical path should follow these *rules*:
        - The path must start with a single slash `'/'`.
        - Directories within the path must be separated by exactly one slash
        `'/'`.
        - The path must not end with a slash `'/'`, unless it is the root
        directory.
        - The path must not have any single or double periods (`'.'` and `'..'`)
        used to denote current or parent directories.

        Return the **simplified canonical path**.

        Args:
            path (str): absolute path for a Unix-style file system

        Returns:
            str: the simplified canonical path.
        """

        dirs = []  # separate directories

        # Split the path on "/" to separate the path into directories, then add
        # the directories to `dirs`.
        for dir in path.split("/"):
            # Empty directories ("//" -> ""), "." directories, and ".."
            # directories are not added to dirs.
            if dir != "" and dir != "." and dir != "..":
                dirs.append(dir)
            ## If dir is "..", remove a directory to get to the parent directory.
            elif dir == ".." and dirs:
                dirs.pop()

        # Rejoin the directories adding slashes between each.
        return "/" + "/".join(dirs)


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        path = "/home/"
        expected = "/home"
        actual = self.sol.simplifyPath(path)
        self.assertEqual(expected, actual)

    def test_example2(self):
        path = "/home//foo/"
        expected = "/home/foo"
        actual = self.sol.simplifyPath(path)
        self.assertEqual(expected, actual)

    def test_example3(self):
        path = "/home/user/Documents/../Pictures"
        expected = "/home/user/Pictures"
        actual = self.sol.simplifyPath(path)
        self.assertEqual(expected, actual)

    def test_example4(self):
        path = "/../"
        expected = "/"
        actual = self.sol.simplifyPath(path)
        self.assertEqual(expected, actual)

    def test_example5(self):
        path = "/.../a/../b/c/../d/./"
        expected = "/.../b/d"
        actual = self.sol.simplifyPath(path)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
