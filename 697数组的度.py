"""
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count, nums_begin, nums_end = {}, {}, {}
        for index in range(len(nums)):
            if nums[index] not in nums_count:
                nums_count[nums[index]] = 1
                nums_begin[nums[index]] = index
            else:
                nums_count[nums[index]] += 1
            nums_end[nums[index]] = index

        max_count = 0
        max_count_num = []
        for num in nums_count:
            if nums_count[num] > max_count:
                max_count = nums_count[num]
                max_count_num = [num]
            elif nums_count[num] == max_count:
                max_count_num.append(num)

        min_length = len(nums)
        for num in max_count_num:
            num_length = nums_end[num] - nums_begin[num] + 1
            if num_length < min_length:
                min_length = num_length

        return min_length
