"""
给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

 

示例：
输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3
最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.min_diff = float('inf')
        self.pre_value = float('-inf')

        def ldr(node):
            if not node:
                return
            ldr(node.left)
            self.min_diff = min(self.min_diff, node.val - self.pre_value)
            self.pre_value = node.val
            ldr(node.right)

        ldr(root)
        return self.min_diff
