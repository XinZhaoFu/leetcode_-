"""
给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = s[0]
        temp_count = 0
        count = []
        res = 0

        for ch in s:
            if ch == last:
                temp_count += 1
            else:
                count.append(temp_count)
                temp_count = 1
                last = ch
        count.append(temp_count)

        for index in range(len(count)-1):
            res += min(count[index], count[index+1])
        return res
