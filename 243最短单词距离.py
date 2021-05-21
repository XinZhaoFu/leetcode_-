"""
给定一个单词列表和两个单词 word1 和 word2，返回列表中这两个单词之间的最短距离。

示例:
假设 words = ["practice", "makes", "perfect", "coding", "makes"]

输入: word1 = “coding”, word2 = “practice”
输出: 3
输入: word1 = "makes", word2 = "coding"
输出: 1
注意:
你可以假设 word1 不等于 word2, 并且 word1 和 word2 都在列表里。
"""


class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_last_index = None
        word2_last_index = None
        min_distance = len(wordsDict)
        for index in range(len(wordsDict)):
            word = wordsDict[index]
            if word == word1:
                word1_last_index = index
            if word == word2:
                word2_last_index = index
            if word1_last_index >= 0 and word2_last_index >= 0:
                min_distance = min(abs(word1_last_index - word2_last_index), min_distance)

        return min_distance
