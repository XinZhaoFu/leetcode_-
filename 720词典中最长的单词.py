"""
给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。

若无答案，则返回空字符串。

示例 1：
输入：
words = ["w","wo","wor","worl", "world"]
输出："world"
解释：
单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
"""


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        temp_record, res = set(), ''
        for word in words:
            if word[:-1] in temp_record or len(word) == 1:
                if len(word) > len(res):
                    res = word
                temp_record.add(word)
        return res
