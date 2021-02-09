"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：
n = 15,
返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if not n:
            return []
        res = [str(num) for num in range(1, n+1)]

        temp3 = 1
        while temp3 * 3 <= n:
            res[temp3 * 3 - 1] = 'Fizz'
            temp3 += 1

        temp5 = 1
        while temp5 * 5 <= n:
            if temp5 % 3 == 0:
                res[temp5 * 5 - 1] = 'FizzBuzz'
            else:
                res[temp5 * 5 - 1] = 'Buzz'
            temp5 += 1

        return res
