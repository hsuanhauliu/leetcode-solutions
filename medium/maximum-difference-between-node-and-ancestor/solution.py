# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        global_max = 0
        curr_q = [(root, root.val, root.val)]
        next_q = []
        while curr_q:
            for node, curr_max, curr_min in curr_q:
                for child in [node.left, node.right]:
                    if child:
                        global_max = max(global_max, abs(curr_max - child.val), abs(curr_min - child.val))
                        next_q.append((child, max(curr_max, child.val), min(curr_min, child.val)))
            curr_q = next_q
            next_q = []
        return global_max