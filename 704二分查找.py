"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p_left = 0
        p_right = len(nums) - 1
        while p_left <= p_right:
            p_mid = (p_left + p_right) // 2
            if nums[p_mid] == target:
                return p_mid
            elif nums[p_mid] < target:
                p_left = p_mid + 1
            else:
                p_right = p_mid - 1
        return -1
