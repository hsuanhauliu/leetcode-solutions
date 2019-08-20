# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        
        if s.val == t.val and self.similar_trees(s, t):
            return True
        
        if self.isSubtree(s.left, t):
            return True
        return self.isSubtree(s.right, t)
    
    
    def similar_trees(self, node_1, node_2):
        if not node_1 and not node_2:
            return True
        
        if (node_1 and node_2 and node_1.val == node_2.val and
            self.similar_trees(node_1.left, node_2.left) and
            self.similar_trees(node_1.right, node_2.right)):
            return True
        return False