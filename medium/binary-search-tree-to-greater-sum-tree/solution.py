# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node, curr):
            if not node:
                return 0
            
            r_val = helper(node.right, curr)
            node.val += r_val + curr
            l_val = helper(node.left, node.val)
            return node.val + l_val - curr
        
        helper(root, 0)
        return root