"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了集合 S 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1：
输入：nums = [1,2,2,4]
输出：[2,3]
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_nums = sum(nums)
        sum_1_n = sum([num for num in range(1, len(nums)+1)])
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return [num, num+(sum_1_n-sum_nums)]
            else:
                nums_dict[num] = 1
