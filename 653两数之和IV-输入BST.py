"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7
Target = 9
输出: True
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        bst_val = []

        def ldr(node):
            if not node:
                return
            ldr(node.left)
            bst_val.append(node.val)
            ldr(node.right)

        ldr(root)
        p_left = 0
        p_right = len(bst_val)-1

        while p_left < p_right:
            if bst_val[p_left] + bst_val[p_right] == k:
                return True
            elif bst_val[p_left] + bst_val[p_right] < k:
                p_left += 1
            else:
                p_right -= 1
        return False
