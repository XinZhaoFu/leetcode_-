"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。

现在，给你一个整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

 

示例 1：

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]

这道题应该用字典来做 但是count函数很少用过 拿来练练手
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = list(set(nums))
        nums_set.sort()
        max_subsequence = 0
        for index in range(1, len(nums_set)):
            if nums_set[index] - nums_set[index-1] == 1:
                temp_max_subsequence = nums.count(nums_set[index]) + nums.count(nums_set[index-1])
                if temp_max_subsequence > max_subsequence:
                    max_subsequence = temp_max_subsequence
        return max_subsequence
