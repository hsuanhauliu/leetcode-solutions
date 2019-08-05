# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        curr_q = [(root, 0)]
        max_w = 0
        while curr_q:
            curr_w = curr_q[-1][1] - curr_q[0][1] + 1
            max_w = max(max_w, curr_w)
            next_q = []
            for node, pos in curr_q:
                if node.left:
                    next_q.append((node.left, 2 * pos))
                if node.right:
                    next_q.append((node.right, 2 * pos + 1))
            curr_q = next_q
        
        return max_w