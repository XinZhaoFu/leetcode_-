"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'
"""


class Solution(object):
    def numIslands_bfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        nums = 0
        queue = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    nums += 1
                    queue.append((row, col))
                    while queue:
                        pop_row, pop_col = queue.pop()
                        grid[pop_row][pop_col] = '0'
                        for temp_row, temp_col in [(pop_row-1, pop_col), (pop_row+1, pop_col), (pop_row, pop_col-1), (pop_row, pop_col+1)]:
                            if 0 <= temp_row < rows and 0 <= temp_col < cols:
                                if grid[temp_row][temp_col] == '1':
                                    queue.append((temp_row, temp_col))

        return nums


    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, rows, cols, row, col):
            grid[row][col] = '0'
            for temp_row, temp_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                if 0 <= temp_row < rows and 0 <= temp_col < cols and grid[temp_row][temp_col] == '1':
                    dfs(grid, rows, cols, temp_row, temp_col)

        rows, cols = len(grid), len(grid[0])
        nums = 0
        queue = []

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    nums += 1
                    dfs(grid, rows, cols, row, col)

        return nums
