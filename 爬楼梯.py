"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if not n: return 0
        if n == 1: return 1
        if n == 2: return 2

        temp_a, temp_b = 1, 2
        for _ in range(n-2):
            temp_c = temp_a + temp_b
            temp_a, temp_b = temp_b, temp_c

        return temp_c
