# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0, 0
            
            l_1, l_2 = helper(node.left)
            r_1, r_2 = helper(node.right)
            curr_1 = node.val + l_2 + r_2
            curr_2 = max(l_1, l_2) + max(r_1, r_2)
            return curr_1, curr_2
        return max(helper(root))
    