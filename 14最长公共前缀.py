"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_length = len(strs)
        if strs_length == 0:
            return ''
        if strs_length == 1:
            return strs[0]

        min_str_length = len(strs[0])
        for strs_element in strs[1:]:
            if min_str_length > len(strs_element):
                min_str_length = len(strs_element)

        common_index = 0
        for str_index in range(min_str_length):
            strs0_value = strs[0][str_index]
            common_index = str_index
            for strs_index in range(1, strs_length):
                if strs[strs_index][str_index] != strs0_value:
                    if common_index == 0:
                        return ''
                    return strs[0][:common_index]

        return strs[0][:min_str_length]
