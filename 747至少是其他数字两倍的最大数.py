"""
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

示例 1:
输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ele = float('-inf')
        second_ele = float('-inf')
        max_index = -1

        for index in range(len(nums)):
            if nums[index] > max_ele:
                max_ele, second_ele, max_index = nums[index], max_ele, index
            elif nums[index] > second_ele:
                second_ele = nums[index]
        if max_ele >= second_ele * 2:
            return max_index
        return -1
