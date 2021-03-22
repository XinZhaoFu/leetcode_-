"""
在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。

输入：[[2]]
输出：5
"""


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        temp_max_row_value_list = [0] * cols
        for row in range(rows):
            temp_max_col_value = 0
            for col in range(cols):
                if grid[row][col] > 0:
                    res += 1
                if grid[row][col] > temp_max_col_value:
                    temp_max_col_value = grid[row][col]
                if grid[row][col] > temp_max_row_value_list[col]:
                    temp_max_row_value_list[col] = grid[row][col]
            res += temp_max_col_value

        res += sum(temp_max_row_value_list)
        return res
