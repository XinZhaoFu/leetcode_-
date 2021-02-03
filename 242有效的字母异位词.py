"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1[i] = dic1.get(i,0) + 1
        for i in t:
            dic2[i] = dic2.get(i,0) + 1
        return dic1 == dic2
