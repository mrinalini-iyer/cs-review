# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isValidBSTLimit(self, root, min, max):
        if root is None: 
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValidBSTLimit(root.left, min, root.val) and self.isValidBSTLimit(root.right, root.val, max)
     
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isValidBSTLimit(root,-float('inf'), float('inf'))
