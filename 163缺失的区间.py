"""
给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：

输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
输出: ["2", "4->49", "51->74", "76->99"]
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if len(nums) == 0:
            if upper > lower:
                return [str(lower) + "->" + str(upper)]
            return [str(lower)]

        res = []

        if nums[0] > lower:
            if nums[0] - lower == 1:
                res.append(str(lower))
            if nums[0] - lower > 1:
                res.append(str(lower) + "->" + str(nums[0] - 1))

        if len(nums) > 1:
            for index in range(1, len(nums)):
                if nums[index] > nums[index - 1]:
                    if nums[index] - nums[index - 1] == 2:
                        res.append(str(nums[index] - 1))
                    if nums[index] - nums[index - 1] > 2:
                        res.append(str(nums[index - 1] + 1) + "->" + str(nums[index] - 1))

        if upper > nums[-1]:
            if upper - nums[-1] == 1:
                res.append(str(upper))
            if upper - nums[-1] > 1:
                res.append(str(nums[-1] + 1) + "->" + str(upper))

        return res
