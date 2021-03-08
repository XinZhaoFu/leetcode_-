"""
给你一个整数数组 nums，请编写一个能够返回数组 “中心下标” 的方法。

数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心下标，返回 -1 。如果数组有多个中心下标，应该返回最靠近左边的那一个。

注意：中心下标可能出现在数组的两端。

示例 1：
输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 (1 + 7 + 3 = 11)，
右侧数之和 (5 + 6 = 11) ，二者相等。
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        right_sum = sum(nums)
        left_sum = 0
        for index in range(len(nums)):
            right_sum -= nums[index]
            if right_sum == left_sum:
                return index
            left_sum += nums[index]

        return -1
