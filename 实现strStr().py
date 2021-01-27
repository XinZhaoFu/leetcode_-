"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串

在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)

如果不存在，则返回  -1
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_haystack < len_needle:
            return -1

        for i_haystack in range(len_haystack-len_needle+1):
            if haystack[i_haystack] == needle[0]:
                if haystack[i_haystack:i_haystack+len_needle] == needle:
                    return i_haystack

        return -1
