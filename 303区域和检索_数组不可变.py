"""
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

示例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        len_nums = len(nums)
        if len_nums == 0:
            return None
        self.sum_nums = [0] * len_nums
        self.sum_nums[0] = nums[0]
        if len_nums > 1:
            for index in range(1, len_nums):
                self.sum_nums[index] = self.sum_nums[index - 1] + nums[index]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sum_nums[j]
        return self.sum_nums[j] - self.sum_nums[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
