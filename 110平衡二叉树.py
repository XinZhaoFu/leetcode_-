"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：true

示例 2：
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

示例 3：
输入：root = []
输出：true
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.flag = 0

        def depth_check(node):
            if not node:
                return 0
            left_depth = depth_check(node.left)
            right_depth = depth_check(node.right)
            if abs(left_depth - right_depth) > 1:
                self.flag = 1
            depth_node = max(left_depth, right_depth) + 1
            return depth_node

        depth_check(root)
        if self.flag == 1:
            return False
        return True
