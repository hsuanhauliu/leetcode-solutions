class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # variables
        depth = 0
        primary = []
        secondary = []

        # if root is not None
        if root:
            primary.append(root)

        # check each level
        while primary:
            depth += 1
            for node in primary:
                if node.left is None and node.right is None:
                    return depth

                if node.left is not None:
                    secondary.append(node.left)
                if node.right is not None:
                    secondary.append(node.right)

            # change secondary to primary
            primary = secondary
            secondary = []

        # just to be safe
        return depth
