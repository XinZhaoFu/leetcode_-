"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],
   1
    \
     2
    /
   2
返回[2].
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue, dict_val = [], {}
        queue.append(root)

        while queue:
            node = queue.pop(0)
            dict_val[node.val] = dict_val.get(node.val, 0) + 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        modes = []
        max_num = 0
        for key in dict_val.keys():
            if dict_val[key] > max_num:
                max_num = dict_val[key]
                modes = [key]
            elif dict_val[key] == max_num:
                modes.append(key)

        return modes
