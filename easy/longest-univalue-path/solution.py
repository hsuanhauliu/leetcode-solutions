# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """ DFS. Bubble up current path length and max path length seen so far.
        
        Time: O(n)
        Space: O(n)
        """
        def dfs(node):
            if not node:
                return 0, 0
            
            left_path, right_path = dfs(node.left), dfs(node.right)
            left_len = left_path[0] + 1 if node.left and node.left.val == node.val else 0
            right_len = right_path[0] + 1 if node.right and node.right.val == node.val else 0
            curr_len = left_len + right_len if node.left and node.right and node.left.val == node.val and node.right.val == node.val else max(left_len, right_len)
            return max(left_len, right_len), max(curr_len, left_path[1], right_path[1])
            
        return dfs(root)[1]