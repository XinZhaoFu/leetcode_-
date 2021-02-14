"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

示例：
输入：
   1
    \
     3
    /
   2
输出：
1
解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val_list = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            val_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        val_list.sort()
        min_diff = val_list[1] - val_list[0]

        for index in range(2, len(val_list)):
            temp = abs(val_list[index] - val_list[index-1])
            if min_diff > temp:
                min_diff = temp
            if min_diff == 0:
                return 0
        return min_diff
