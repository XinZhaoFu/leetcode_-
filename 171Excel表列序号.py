"""
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        base = 1
        res = 0
        s_list = list(s)

        while s_list:
            ch = s_list.pop()
            res += (ord(ch) - 64) * base
            base *=26

        return res
