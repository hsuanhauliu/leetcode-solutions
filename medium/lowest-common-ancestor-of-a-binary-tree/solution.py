# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """ DFS with early stopping.
        As soon as we find a node with both p, q as descendants, we return that node
        and stop the traversing.
        
        Time: O(n)
        Space: O(1)
        """
        def findCommonAncestors(node):
            if not node:
                return (0, None)
            
            l = findCommonAncestors(node.left)
            if l[0] == 2:
                return l
            
            r = findCommonAncestors(node.right)
            if r[0] == 2:
                return r
            
            total = l[0] + r[0] + (node == p or node == q)
            return (total, node) if total == 2 else (total, None)

        return findCommonAncestors(root)[1]
