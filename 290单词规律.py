"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false
"""


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        dict_pattern_s = {}
        dict_s_pattern = {}
        s = s.split(' ')
        if len(pattern) != len(s):
            return False

        for ch, word in zip(pattern, s):
            if (ch in dict_pattern_s and dict_pattern_s[ch] != word) or (word in dict_s_pattern and dict_s_pattern[word] != ch):
                return False
            dict_pattern_s[ch] = word
            dict_s_pattern[word] = ch

        return True
