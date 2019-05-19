# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """ DFS solution
        Time: O(n + m)
        Space: O(n + m)
        
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def getLeaves(node, l):
            if not node:
                return
            
            if not node.left and not node.right:
                l.append(node.val)
                return
            
            getLeaves(node.left, l)
            getLeaves(node.right, l)
        
        sequence_1 = []
        sequence_2 = []
        getLeaves(root1, sequence_1)
        getLeaves(root2, sequence_2)
        
        return self.isSimilar(sequence_1, sequence_2)
        
    
    def isSimilar(self, s_1, s_2):
        if len(s_1) != len(s_2):
            return False
        
        for i in range(len(s_1)):
            if s_1[i] != s_2[i]:
                return False
        
        return True