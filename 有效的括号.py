"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']

        s_list = list(s)
        stack = []

        while s_list:
            s0 = s_list[0]
            if s0 in open_brackets:
                stack.append(s0)
                s_list.remove(s0)
            else:
                close_bracket_index = close_brackets.index(s0)
                if len(stack) == 0:
                    return False
                else:
                    open_bracket_index = open_brackets.index(stack[-1])
                if close_bracket_index != open_bracket_index:
                    return False
                else:
                    s_list.remove(s0)
                    stack.pop()

        return len(stack) == 0





