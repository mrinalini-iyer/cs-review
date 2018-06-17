# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        answer = []
        node = TreeNode(0)  
        if root is None:
            return answer      
        q = [root]
        while(q):
            temp = []
            sum = 0
            count = 0
            while(q):
                node = q.pop()
                sum += node.val
                count+= 1
                
                if(node.left is not None):
                    temp.append(node.left)
                if(node.right is not None):
                    temp.append(node.right)
            q = temp
            answer.append(sum * 1.0/ count)
        return answer     
