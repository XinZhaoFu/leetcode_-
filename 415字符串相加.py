"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

提示：
num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return num2 or num1
        if len(num1) < len(num2):
            num1 , num2 = num2, num1

        dict_num = {}
        for i in range(10):
            dict_num[str(i)] = i

        flag = 0
        res = ''
        len_num1 = len(num1)
        len_num2 = len(num2)
        num2 = '0' * (len_num1 - len_num2) + num2
        for index in range(len_num1):
            n1 = dict_num[num1[len_num1 - 1 - index]]
            n2 = dict_num[num2[len_num1 - 1 - index]]
            temp_res = n1 + n2 + flag
            flag = temp_res // 10
            res = str(temp_res % 10) + res
        if flag:
            res = '1' + res
        return res
