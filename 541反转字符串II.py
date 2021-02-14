"""
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        index = 0
        while index + k * 2 <= len(s):
            temp = s[index:index+k]
            res = res + temp[::-1] + s[index+k:index+k*2]
            index += k * 2
        if len(s) - index == 0:
            return res
        if len(s) - index < k:
            temp = s[index:]
            res += temp[::-1]
        if len(s) - index >= k:
            temp = s[index:index+k]
            res  = res + temp[::-1] + s[index+k:]
        return res
