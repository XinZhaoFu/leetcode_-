"""
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        queue = []
        queue_depth = [1]
        queue.append(root)

        while queue:
            depth = queue_depth.pop(0)
            node = queue.pop(0)
            if not node.left and not node.right:
                return depth
            else:
                depth += 1
                if node.left:
                    queue.append(node.left)
                    queue_depth.append(depth)
                if node.right:
                    queue.append(node.right)
                    queue_depth.append(depth)


