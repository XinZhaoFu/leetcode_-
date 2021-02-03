"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        len_nums = len(nums)
        zero_num = len_nums - index
        zero_list = [0] * zero_num
        nums[len_nums-zero_num: len_nums] = zero_list
        return nums
