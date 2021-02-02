"""
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b

示例：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        len_nums = len(nums)
        if len_nums < 2:
            return [str(nums[0])]

        res = []
        temp_res = ''
        index = 0
        while index < len_nums-1:
            if nums[index+1] - nums[index] == 1:
                if temp_res == '':
                    temp_res = temp_res + str(nums[index]) + '->'
            else:
                if temp_res == '':
                    res.append(str(nums[index]))
                else:
                    temp_res += str(nums[index])
                    res.append(temp_res)
                    temp_res = ''
            index += 1

        if temp_res == '':
            res.append(str(nums[-1]))
        else:
            temp_res += str(nums[-1])
            res.append(temp_res)

        return res

