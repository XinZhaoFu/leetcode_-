"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true

示例 2:
输入: 16
输出: true

示例 3:
输入: 218
输出: false
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        return (n & (n - 1)) == 0
