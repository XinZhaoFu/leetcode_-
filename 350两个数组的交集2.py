"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""
import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        set_nums1 = collections.Counter(nums1)
        set_nums2 = collections.Counter(nums2)

        for num in set_nums1:
            if num in set_nums2:
                res += [num] * min(set_nums1[num], set_nums2[num])
        return res
