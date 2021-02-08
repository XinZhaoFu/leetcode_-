"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1：
输入："hello"
输出："holle"

示例 2：
输入："leetcode"
输出："leotcede"
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        left = 0
        right = len(s) - 1
        s_list = list(s)

        while left < right:
            if s_list[left] not in vowels:
                left += 1
            if s_list[right] not in vowels:
                right -= 1
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        s = ''.join(s_list)
        return s
