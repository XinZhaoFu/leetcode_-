"""
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        res = []
        queue = []
        queue.append(root)

        while queue:
            temp_queue = []
            temp_val_queue = []
            len_queue = len(queue)
            for _ in range(len_queue):
                node = queue.pop(0)
                temp_val_queue.append(node.val)

                if node.left:
                    temp_queue.append(node.left)

                if node.right:
                    temp_queue.append(node.right)

            queue.extend(temp_queue)
            res.extend([temp_val_queue])

        res.reverse()
        return res
