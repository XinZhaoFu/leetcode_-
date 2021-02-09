"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

示例 1：
输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return max(nums)

        set_nums = set(nums)
        list_nums = list(set_nums)
        if len(list_nums) < 3:
            return max(list_nums)
        list_nums.remove(max(list_nums))
        list_nums.remove(max(list_nums))
        return max(list_nums)
