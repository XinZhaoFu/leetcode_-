"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums: return 0

        length_nums = len(nums)
        if length_nums == 1: return nums[0]

        for index in range(1, length_nums):
            nums_index = nums[index]
            nums[index] = max(nums[index-1]+nums_index, nums_index)

        return max(nums)
