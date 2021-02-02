"""
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pre_p = None
        cur_p = head

        while cur_p:
            next_p = cur_p.next
            cur_p.next = pre_p
            pre_p = cur_p
            cur_p = next_p
        return pre_p


