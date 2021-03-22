"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_list = []
        t_list = []

        for ch in S:
            if ch == '#':
                if len(s_list) != 0:
                    s_list.pop()
            else:
                s_list.append(ch)

        for ch in T:
            if ch == '#':
                if len(t_list) != 0:
                    t_list.pop()
            else:
                t_list.append(ch)

        return s_list == t_list
