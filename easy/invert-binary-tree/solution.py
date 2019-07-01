# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        curr_q = [root]
        next_q = []
        while curr_q:
            for node in curr_q:
                node.left, node.right = node.right, node.left
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)
            curr_q = next_q
            next_q = []
        
        return root