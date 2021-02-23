"""
包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:
输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
"""


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        cols = len(M[0])

        res = []
        for row in range(rows):
            temp_res = []
            for col in range(cols):
                count = 0
                temp_sum = 0
                for x in (row - 1, row, row + 1):
                    for y in (col - 1, col, col + 1):
                        if 0 <= x < rows and 0 <= y < cols:
                            count += 1
                            temp_sum += M[x][y]
                temp_sum = temp_sum / count
                temp_res.append(temp_sum)
            res.append(temp_res)
        return res
