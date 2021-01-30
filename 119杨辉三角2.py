"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:return [1]

        row = [1]
        index_value = rowIndex + 1
        for row_index in range(1, index_value):
            row.insert(0, 0)
            for col_index in range(row_index):
                row[col_index] = row[col_index] + row[col_index + 1]

        return row

