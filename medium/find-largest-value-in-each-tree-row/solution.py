# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        curr_q = [root]
        while curr_q:
            next_q = []
            maximum = -float('inf')
            for node in curr_q:
                maximum = max(maximum, node.val)
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            res.append(maximum)
            curr_q = next_q
            
        return res