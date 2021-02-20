"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        temp_queue = []
        res = []
        temp_res = 0
        temp_val = []

        while queue or temp_queue:
            if not queue:
                temp_res = sum(temp_val)*1. / len(temp_val)
                res.append(temp_res)
                queue = temp_queue
                temp_queue, temp_val = [], []
            node = queue.pop(0)
            temp_val.append(node.val)
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        if not temp_queue:
            temp_res = sum(temp_val)*1. / len(temp_val)
            res.append(temp_res)
        return res
