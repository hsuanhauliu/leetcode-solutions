# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """ BFS
        Time: O(n)
        Space: O(n)
        """
        if not root:
            return False
        
        curr_q = [(root, 0)]
        found, prev_parent_v = False, 0
        
        while curr_q:
            next_q = []
            for node, parent_v in curr_q:
                if node.val == x or node.val == y:
                    if found:
                        return prev_parent_v != parent_v
                    found = True
                    prev_parent_v = parent_v
                    
                if node.left:
                    next_q.append((node.left, node.val))
                    
                if node.right:
                    next_q.append((node.right, node.val))
            if found:
                return False
            curr_q = next_q
        return False