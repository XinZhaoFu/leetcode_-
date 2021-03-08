"""
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：
输入：
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []

        for num in range(left, right+1):
            if num >= 10:
                element_record = set()
                temp_num = num
                while temp_num:
                    element_record.add(temp_num%10)
                    temp_num /= 10

                flag = True
                for ele in element_record:
                    if ele == 0 or num % ele != 0:
                        flag = False
                        break
                if flag:
                    res.append(num)
            else:
                res.append(num)
        return res
