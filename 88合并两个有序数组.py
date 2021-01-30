"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1_pointer = m - 1
        nums2_pointer = n - 1

        len_nums = m + n

        for index in reversed(range(len_nums)):
            if nums1_pointer < 0 or nums2_pointer < 0:
                break
            if nums1[nums1_pointer] >= nums2[nums2_pointer]:
                nums1[index] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[index] = nums2[nums2_pointer]
                nums2_pointer -= 1

        if nums2_pointer >= 0:
            nums1[:nums2_pointer+1] = nums2[:nums2_pointer+1]
        return nums1

