# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """ Breadth first search
        Add nodes from right to left. At each level, append the value
        of the right-most node to our output queue.
        
        Time: O(n)
        Space: O(n)
        """
        res = []
        curr_q = []
        if root:
            curr_q.append(root)
            
        while curr_q:
            next_q = []
            res.append(curr_q[0].val)
            for node in curr_q:
                if node.right:
                    next_q.append(node.right)
                if node.left:
                    next_q.append(node.left)
            curr_q = next_q
        
        return res