class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # base case: no root
        if root is None:
            return 0

        # go deeper to find leaf nodes
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
