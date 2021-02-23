"""
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例：
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if not nums:
            return 0
        if k == 1:
            return max(nums)
        if k == len(nums):
            return sum(nums) * 1.0 / k
        max_sum = sum(nums[:k])
        temp_sum = sum(nums[:k])
        for index in range(k, len(nums)):
            temp_sum = temp_sum - nums[index-k] + nums[index]
            max_sum = max(temp_sum, max_sum)
        return max_sum * 1.0 / k
