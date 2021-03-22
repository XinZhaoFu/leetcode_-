"""
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：
输入：[1,2,2,3]
输出：true
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag = 0 # 1为增 -1为减
        for index in range(1, len(A)):
            if A[index-1] < A[index]:
                if flag == -1:
                    return False
                if flag == 0:
                    flag = 1
            if A[index-1] > A[index]:
                if flag == 1:
                    return False
                if flag == 0:
                    flag = -1
        return True

