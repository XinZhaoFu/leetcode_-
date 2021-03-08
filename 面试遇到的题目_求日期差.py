"""
面试遇到的题目 给出两日期字符串 求两日期相差时间
eg: 20201010 30300909
面试的时候想了半天‘差值’的英文是什么 最后百度的

思路是先求2020年到3030年 不含3030年 一共有多少天 再减去2020年这一年度过了多少天 再加上3030年度过的天数
"""


def data_subtraction(data1, data2):
    """
    eg:19951111 19960101
        return 52
    日期相减 返回相隔时长
    :param data1: type:str
    :param data2: type:str
    :return: type:int
    """

    def spend_day(year, month, day):
        """
        返回该天是该年的第几天
        :param year:
        :param month:
        :param day:
        :return:
        """
        sum_day = 0
        month_thirty_one = [1, 3, 5, 7, 8, 10, 12]
        if year % 4 == 0:
            two_month_day = 29
        else:
            two_month_day = 28

        # 循环中求的是前month-1个月都有多少天
        for m in range(month):
            if m in month_thirty_one:
                sum_day += 31
            elif m == 2:
                sum_day += two_month_day
            else:
                sum_day += 30
        sum_day += day

        return sum_day

    year1, year2 = int(data1[:4]), int(data2[:4])
    month1, month2 = int(data1[4:6]), int(data2[4:6])
    day1, day2 = int(data1[7:]), int(data2[7:])
    sum_day = 0
    for year in range(year1, year2):
        if year % 4 == 0:
            sum_day += 366
        else:
            sum_day += 356
    return sum_day - spend_day(year1, month1, day1) + spend_day(year2, month2, day2)

