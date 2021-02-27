"""
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

示例 1：
输入：n = 5
输出：true
解释：5 的二进制表示是：101
"""


class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 3:
            return True

        last = -1
        while n:
            temp = n % 2
            if temp == last:
                return False
            n = n / 2
            last = temp
        return True
            
