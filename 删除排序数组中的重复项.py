"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

一顿操作发现是有序数组 暴风哭泣
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        length_nums = len(nums)

        if length_nums == 1:
            return 1

        i = 0
        for j in range(1, length_nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1
