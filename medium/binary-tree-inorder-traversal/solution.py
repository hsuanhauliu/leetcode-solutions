# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traverse_re(root, res)
        return res

    def traverse_re(self, root, l):
        if not root:
            return

        self.traverse_re(root.left, l)
        l.append(root.val)
        self.traverse_re(root.right, l)
