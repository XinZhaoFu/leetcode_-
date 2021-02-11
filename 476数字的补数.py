"""
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。

示例 1:
输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。

示例 2:
输入: 1
输出: 0
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        res = 1

        while res < num:
            res = res << 1
            res += 1

        return res ^ num


"""
    def all_ones(x):
    x |= x >> 1
    x |= x >> 2
    x |= x >> 4
    x |= x >> 8
    x |= x >> 16
    return x
"""
