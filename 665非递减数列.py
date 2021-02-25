"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def is_sort(nums):
            for index in range(1, len(nums)):
                if nums[index-1] > nums[index]:
                    return False
            return True

        for index in range(len(nums)-1):
            if nums[index] > nums[index+1]:
                temp = nums[index]
                nums[index] = nums[index+1]
                if is_sort(nums):
                    return True
                else:
                    nums[index] = nums[index+1] = temp
                return is_sort(nums)
        return True
