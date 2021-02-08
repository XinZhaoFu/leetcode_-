"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0
s = "loveleetcode"
返回 2
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_s = {}
        for ch in s:
            hash_s[ch] = hash_s.get(ch, 0) + 1

        if not 1 in hash_s.values():
            return -1

        for index in range(len(s)):
            if hash_s[s[index]] == 1:
                return index
