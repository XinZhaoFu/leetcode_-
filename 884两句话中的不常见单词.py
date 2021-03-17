"""
给定两个句子 A 和 B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）

如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。

返回所有不常用单词的列表。

您可以按任何顺序返回列表。

示例 1：
输入：A = "this apple is sweet", B = "this apple is sour"
输出：["sweet","sour"]
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_split_list = A.split()
        b_split_list = B.split()
        word_list = a_split_list + b_split_list
        res = []

        word_dict = {}
        for word in word_list:
            word_dict[word] = word_dict.get(word, 0) + 1

        for word in word_dict:
            if word_dict[word] == 1:
                res.append(word)

        return res
