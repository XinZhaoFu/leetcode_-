"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def is_palindrome(s, index):
            if index == 0:
                temp_s = s[1:]
            elif index == len(s):
                temp_s = s[:-1]
            else:
                temp_s = s[:index] + s[index+1:]
            return temp_s[::-1] == temp_s

        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if is_palindrome(s, left) or is_palindrome(s, right):
                    return True
                return False
        return True
