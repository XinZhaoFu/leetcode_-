"""
整数反转

给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if -10 < x < 10:
            return x

        if x < -(2 ** 31) or x > (2 ** 31 - 1):
            return 0

        flag = 0
        if x < 0:
            x = -x
            flag = 1

        result = 0
        while x:
            result = result * 10 + x % 10
            x = x // 10

        if flag:
            result = -result

        if result < -(2 ** 31) or result > (2 ** 31 - 1):
            return 0

        return result
