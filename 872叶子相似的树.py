"""
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；
否则返回 false 。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_list1 = []
        leaf_list2 = []

        def dlr(node, leaf_list):
            if not node:
                return
            if not node.left and not node.right:
                leaf_list.append(node.val)
            dlr(node.left, leaf_list)
            dlr(node.right, leaf_list)

        dlr(root1, leaf_list1)
        dlr(root2, leaf_list2)

        return leaf_list1 == leaf_list2
