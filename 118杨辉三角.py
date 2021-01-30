"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: return []
        res = [[1]]
        temp_out_row_res = [1]
        for row in range(1, numRows):
            temp_now_row_res = [1]
            for col in range(1, row):
                temp_now_row_res.append(temp_out_row_res[col-1]+temp_out_row_res[col])
            temp_now_row_res.append(1)
            res.append(temp_now_row_res)
            temp_out_row_res = temp_now_row_res
        return res
