# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        """ Delete nodes from bottom-up using DFS.
        
        Time: O(n)
        Space: O(n)
        """
        res = []
        if self.find_trees(root, set(to_delete), res):
            res.append(root)
        return res
    
    
    def find_trees(self, node, to_delete, trees):
        if not node:
            return False
        
        l = self.find_trees(node.left, to_delete, trees)
        r = self.find_trees(node.right, to_delete, trees)
        
        if node.val in to_delete:
            if l:
                trees.append(node.left)
            if r:
                trees.append(node.right)
            return False
        
        if not l:
            node.left = None
        if not r:
            node.right = None
        return True