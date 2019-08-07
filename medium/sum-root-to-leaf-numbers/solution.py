# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def get_paths(node, parent, res):
            if not node:
                return
            
            curr_val = parent * 10 + node.val
            if not node.left and not node.right:
                res.append(curr_val)
                return
            
            get_paths(node.left, curr_val, res)
            get_paths(node.right, curr_val, res)
            
        res = []
        get_paths(root, 0, res)
        return sum(res)
        