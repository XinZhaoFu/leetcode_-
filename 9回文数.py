"""
回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        res = 0
        while x > res:
            res = res * 10 + x % 10
            x = x // 10

        if x < res:
            res = res // 10

        return x == res
