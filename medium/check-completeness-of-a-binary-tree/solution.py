# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """ BFS

        Time: O(n)
        Spce: O(n)
        """
        curr_q = [(root, 0)]
        level = 0
        while curr_q:
            # make sure all nodes are as far left as possible
            if len(curr_q) - 1 != curr_q[-1][1]:
                return False

            next_q = []
            for node, pos in curr_q:
                if not node.left and node.right:
                    return False

                if node.left:
                    next_q.append((node.left, 2*pos))

                if node.right:
                    next_q.append((node.right, 2*pos + 1))

            # if there are more nodes below, the current level has to be full
            if next_q and len(curr_q) != 2 ** level:
                return False

            curr_q = next_q
            level += 1

        return True
