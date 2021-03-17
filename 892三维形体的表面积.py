"""
给你一个 n * n 的网格 grid ，上面放置着一些 1 x 1 x 1 的正方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。

请你返回最终这些形体的总表面积。

注意：每个形体的底面也需要计入表面积中。

示例 ：
输入：grid = [[2]]
输出：10
"""


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    res += 2
                    for temp_row, temp_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                        if 0 <= temp_row < rows and 0 <= temp_col < cols:
                            temp_value = grid[temp_row][temp_col]
                        else:
                            temp_value = 0
                        res += max(grid[row][col] - temp_value, 0)
        return res
