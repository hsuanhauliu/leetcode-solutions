# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        curr_q = [(root, 0)]
        next_q = []
        total = 0
        while curr_q:
            for node, curr in curr_q:
                curr = (curr << 1) + node.val
                if not node.left and not node.right:
                    total += curr
                if node.left:
                    next_q.append((node.left, curr))
                if node.right:
                    next_q.append((node.right, curr))
            curr_q = next_q
            next_q = []
        
        return total