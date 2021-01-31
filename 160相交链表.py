"""
编写一个程序，找到两个单链表相交的起始节点。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None

        len_headA = 0
        cur1, cur2 = headA, headB
        while cur1:
            len_headA += 1
            cur1 = cur1.next
        len_headB = 0
        while cur2:
            len_headB += 1
            cur2 = cur2.next

        diff = abs(len_headB - len_headA)
        len_common = min(len_headA, len_headB)

        if len_headA > len_headB:
            headA, headB = headB, headA

        for _ in range(diff):
            headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headB
