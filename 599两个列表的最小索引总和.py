"""
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
"""


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        dict_list = {}
        min_index = len(list1) + len(list2)
        for index in range(len(list1)):
            dict_list[list1[index]] = index
        for index in range(len(list2)):
            if list2[index] in dict_list:
                sum_index = index + dict_list[list2[index]]
                if sum_index < min_index:
                    res = [list2[index]]
                    min_index = sum_index
                elif sum_index == min_index:
                    res.append(list2[index])
        return res
