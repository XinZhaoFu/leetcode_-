"""
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        count_and_say = '1'

        for _ in range(n-1):
            count_and_say_length = len(count_and_say)
            temp_count_and_say = ''
            temp_count = 1
            index = 0
            while index < count_and_say_length:
                while (index+temp_count) < count_and_say_length and count_and_say[index] == count_and_say[index+temp_count]:
                    temp_count += 1
                temp_count_and_say = temp_count_and_say + str(temp_count) + count_and_say[index]

                index += temp_count
                temp_count = 0
            count_and_say = temp_count_and_say

        return count_and_say
