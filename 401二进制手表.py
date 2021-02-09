"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。
给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。

示例：
输入: n = 1
返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
"""


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hour = {1: [1, 2, 4, 8],
                2: [3, 5, 9, 6, 10],
                3: [7, 11],
                0: [0]}
        minute = {1: [1, 2, 4, 8, 16, 32],
                  2: [3, 5, 9, 17, 33, 6, 10, 18, 34, 12, 20, 36, 24, 40, 48],
                  3: [7, 11, 19, 35, 13, 21, 37, 25, 41, 49, 14, 22, 38, 26, 42, 50, 28, 44, 56, 52],
                  4: [15, 23, 39, 27, 29, 30, 43, 45, 46, 51, 53, 54, 57, 58],
                  5: [31, 47, 55, 59],
                  0: [0]}
        res = []
        for i in range(num + 1):
            j = num - i
            if i in hour and j in minute:
                for h in hour[i]:
                    for m in minute[j]:
                        res.append('%d:%02d' % (h, m))
        return res
