# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        vals = []
        self.traverse_inorder_recursive(root, vals)

        for i in range(1, len(vals)):
            if vals[i - 1] >= vals[i]:
                return False
        return True

    def traverse_inorder_recursive(self, root, vals):
        if root:
            self.traverse_inorder_recursive(root.left, vals)
            vals.append(root.val)
            self.traverse_inorder_recursive(root.right, vals)