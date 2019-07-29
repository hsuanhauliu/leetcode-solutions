# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(node, curr_path):
            if not node:
                return curr_path
            
            curr_path = chr(97 + node.val) + curr_path
            if not node.left and not node.right:
                return curr_path
            
            if not node.left:
                return dfs(node.right, curr_path)
            
            if not node.right:
                return dfs(node.left, curr_path)
            
            left_path = dfs(node.left, curr_path)
            right_path = dfs(node.right, curr_path)
            if left_path < right_path:
                return left_path
            return right_path
        return dfs(root, "")