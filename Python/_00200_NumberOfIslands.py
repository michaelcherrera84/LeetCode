from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Given an `m x n` 2D binary grid `grid` which represents a map of
        `'1'`s (land) and `'0'`s (water), return *the number of islands*.

        An **island** is surrounded by water and is formed by connecting
        adjacent lands horizontally or vertically. You may assume all four edges
        of the grid are all surrounded by water.

        Args:
            grid (List[List[str]]): the 2D binary grid

        Returns:
            int: the number of islands
        """

        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            """Map an island by changing "1"s to "#"s.

            Args:
                r (int): row index of the grid
                c (int): column index of the grid
            """

            # Stop mapping if we hit water or the edge of the grid.
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return

            # Map this part of the island.
            grid[r][c] = "#"

            # Continue searching for more connected land.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse the grid in search of islands.
        for r in range(rows):
            for c in range(cols):
                # If we find an island, count it, and "map" it (set "1" to "#").
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        # Reset the grid if needed
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "#":
        #             grid[r][c] = "1"

        return islands


import unittest


class Test_Solution(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        actual = self.sol.numIslands(grid)
        self.assertEqual(expected, actual)

    def test_example2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        actual = self.sol.numIslands(grid)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
