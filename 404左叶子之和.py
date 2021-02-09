"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_sum = 0

        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    left_sum += node.left.val
                else:
                    queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return left_sum


