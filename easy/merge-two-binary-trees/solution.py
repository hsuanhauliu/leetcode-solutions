# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def merge(a, b, c, direction):
            if not a and not b:
                return
            a_val = a.val if a else 0
            b_val = b.val if b else 0
            sum_val = a_val + b_val
            c_next = None
            if direction == 'l':
                c.left = TreeNode(sum_val)
                c_next = c.left
            else:
                c.right = TreeNode(sum_val)
                c_next = c.right
            a_next = a.left if a else None
            b_next = b.left if b else None
            merge(a_next, b_next, c_next, 'l')
            a_next = a.right if a else None
            b_next = b.right if b else None
            merge(a_next, b_next, c_next, 'r')
            
        dummy = TreeNode(0)
        merge(t1, t2, dummy, 'l')
        return dummy.left