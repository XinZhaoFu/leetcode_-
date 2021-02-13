"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

美式键盘 中：

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        dict_keyboard = {}
        for ch in 'qwertyuiopQWERTYUIOP':
            dict_keyboard[ch] = 1
        for ch in 'asdfghjklASDFGHJKL':
            dict_keyboard[ch] = 2
        for ch in 'zxcvbnmZXCVBNM':
            dict_keyboard[ch] = 3

        res = [word for word in words]
        for word in words:
            temp_flag = dict_keyboard[word[0]]
            for ch in word:
                if temp_flag != dict_keyboard[ch]:
                    res.remove(word)
                    break
        return res
