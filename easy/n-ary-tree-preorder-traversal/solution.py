"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """ Use Stack of queues to go through iteratively """
        if not root:
            return []
        
        res = []
        stack = [[root]]
        while stack:
            curr_q = stack[-1]
            curr_node = curr_q[0]
            res.append(curr_node.val)
            if len(curr_q) == 1:
                stack.pop() # remove queue with one element
            else:
                curr_q.pop(0)
            
            if curr_node.children:
                stack.append(curr_node.children[:])
        
        return res