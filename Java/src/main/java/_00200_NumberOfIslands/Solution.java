package _00200_NumberOfIslands;

public class Solution {

    /**
     * Given an {@code m x n} 2D binary grid {@code grid} which represents a map of
     * {@code '1'}s (land) and {@code '0'}s (water), return <i>the number of
     * islands.</i>
     * <p>
     * An <b>island</b> is surrounded by water and is formed by connecting adjacent
     * lands horizontally or vertically. You may assume all four edges of the grid
     * are all surrounded by water.
     * 
     * @param grid the 2D binary grid
     * @return the number of islands
     */
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;

        // Search each grid space for land.
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                // If land is found, add an island, and "map" it.
                if (grid[r][c] == '1') {
                    islands++;
                    mapIsland(grid, r, c);
                }
            }
        }

        return islands;
    }

    /**
     * Map an island by finding all land connected to a starting position. Mark each
     * space as visited land by changing the '1's to '#'s.
     * 
     * @param grid the ocean grid
     * @param r    the row where the land begins
     * @param c    the column where the land begins
     */
    private void mapIsland(char[][] grid, int r, int c) {
        // Stop mapping if we hit the water (or the edge of the grid).
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1')
            return;

        // Map the land.
        grid[r][c] = '#';

        // Search for more connected land.
        mapIsland(grid, r + 1, c);
        mapIsland(grid, r - 1, c);
        mapIsland(grid, r, c + 1);
        mapIsland(grid, r, c - 1);
    }
}
