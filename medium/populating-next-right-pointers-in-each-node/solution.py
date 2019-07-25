"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        curr_q = [root]
        while curr_q:
            next_q = []
            size = len(curr_q)
            for i, node in enumerate(curr_q):
                if node.left and node.right:
                    next_q.append(node.left)
                    next_q.append(node.right)
            
                if i + 1 < size:
                    curr_q[i].next = curr_q[i + 1]
            
            curr_q = next_q
        return root