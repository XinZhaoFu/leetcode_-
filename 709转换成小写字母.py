"""
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

示例 1：
输入: "Hello"
输出: "hello"
"""


class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        temp = ord('a') - ord('A')
        A_ascii = ord('A')
        Z_ascii = ord('Z')
        for ch in str:
            if A_ascii <= ord(ch) <= Z_ascii:
                res += chr(ord(ch)+temp)
            else:
                res += ch
        return res
