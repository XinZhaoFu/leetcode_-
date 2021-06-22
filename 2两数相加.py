"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]

示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_cur, l2_cur = l1, l2
        l1_len, l2_len = 0, 0
        while l1_cur:
            l1_cur = l1_cur.next
            l1_len += 1
        while l2_cur:
            l2_cur = l2_cur.next
            l2_len += 1

        if l1_len < l2_len:
            l1, l2 = l2, l1

        list_node = l1
        list_end = None
        flag = 0

        while l2:
            if flag == 1:
                temp_val = l1.val + l2.val + flag
            else:
                temp_val = l1.val + l2.val

            if temp_val < 10:
                l1.val = temp_val
                flag = 0
            else:
                flag = 1
                l1.val = temp_val % 10

            list_end = l1
            l1 = l1.next
            l2 = l2.next

        while l1:
            if flag == 1:
                temp_val = l1.val + flag
            else:
                temp_val = l1.val
            if temp_val < 10:
                l1.val = temp_val
                flag = 0
            else:
                flag = 1
                l1.val = 0
            list_end = l1
            l1 = l1.next

        if flag:
            list_end.next = ListNode(1)

        return list_node
