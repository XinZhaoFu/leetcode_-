"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"
示例 2:
输入: -7
输出: "-10"
"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if abs(num) < 7:
            return str(num)
        flag = 0
        if num < 0:
            flag = 1
            num = -num
        res = ''
        while num:
            res += str(num%7)
            num /= 7
        if flag:
            return '-' + res[::-1]
        return res[::-1]
