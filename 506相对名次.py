"""
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
"""


class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        dict_score_index = {}
        for index in range(len(score)):
            dict_score_index[score[index]] = index
        score.sort(reverse=True)
        res = [''] * len(score)
        res[dict_score_index[score[0]]] = 'Gold Medal'
        if len(score) > 1:
            res[dict_score_index[score[1]]] = 'Silver Medal'
        if len(score) > 2:
            res[dict_score_index[score[2]]] = 'Bronze Medal'
        for index in range(3, len(score)):
           res[dict_score_index[score[index]]] = str(index+1)
        return res
