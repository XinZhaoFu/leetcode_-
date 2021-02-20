"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1 or not root2:
            return root2 or root1
        queue_root1 = [root1]
        queue_root2 = [root2]

        while queue_root1:
            node1 = queue_root1.pop(0)
            node2 = queue_root2.pop(0)

            node1.val += node2.val
            if node1.left and node2.left:
                queue_root1.append(node1.left)
                queue_root2.append(node2.left)
            elif not node1.left and node2.left:
                node1.left = node2.left

            if node1.right and node2.right:
                queue_root1.append(node1.right)
                queue_root2.append(node2.right)
            elif not node1.right and node2.right:
                node1.right = node2.right
        return root1
