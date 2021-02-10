"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # return s in (s+s)[1:-1]

        s_len = len(s)
        if s_len < 2:
            return False
        temp_s_length = 1
        temp_s = s[0]
        temp_s_num = 0
        s_index = 0

        while s_index < s_len:
            if s_index + temp_s_length > s_len:
                return False
            if s[s_index:s_index + temp_s_length] == temp_s:
                s_index += temp_s_length
                temp_s_num += 1
            else:
                temp_s_length += 1
                temp_s = s[:temp_s_length]
                s_index = 0
                temp_s_num = 0
        return temp_s_num > 1
