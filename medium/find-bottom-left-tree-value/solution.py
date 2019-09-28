# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """ Recursive DFS solution.

        Time: O(n)
        Space: O(1)
        """
        def helper(node, curr_level, curr_best):
            if not node:
                return

            if not node.left and not node.right and curr_level > curr_best[1]:
                curr_best[0] = node.val
                curr_best[1] = curr_level
                return

            helper(node.left, curr_level + 1, curr_best)
            helper(node.right, curr_level + 1, curr_best)

        curr = [0, -1]
        helper(root, 0, curr)
        return curr[0]
