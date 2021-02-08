"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

示例 1：
输入：n = 27
输出：true

示例 2：
输入：n = 0
输出：false
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 3:
            return False

        while n > 1:
            if n % 3:
                return False
            n /= 3
        return n == 1
