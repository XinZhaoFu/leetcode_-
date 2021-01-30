"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits: return 1

        flag = 1
        len_digits = len(digits)

        for index in reversed(range(len_digits)):
            if flag:
                digits[index] += 1
                flag = 0
            if digits[index] > 9:
                digits[index] = digits[index] % 10
                flag = 1

        if flag:
            digits = [1] + digits

        return digits
            
