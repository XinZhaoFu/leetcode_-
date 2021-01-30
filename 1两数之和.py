"""
两数之和

给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) < 2:
            return None

        nums_index = nums.index

        for num in nums:
            temp = target - num
            num_index = nums_index(num)
            if temp in nums[num_index+1:]:
                temp_index = nums[num_index+1:].index(temp) + (num_index + 1)
                return [num_index, temp_index]

        return None
