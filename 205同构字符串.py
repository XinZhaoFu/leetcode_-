"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

示例 1:
输入：s = "egg", t = "add"
输出：true

示例 2：
输入：s = "foo", t = "bar"
输出：false

示例 3：
输入：s = "paper", t = "title"
输出：true
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False

        s_t_replace_dict = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s not in s_t_replace_dict:
                if ch_t in s_t_replace_dict.values():
                    return False
                s_t_replace_dict[ch_s] = ch_t
            if ch_t != s_t_replace_dict[ch_s]:
                return False

        return True

