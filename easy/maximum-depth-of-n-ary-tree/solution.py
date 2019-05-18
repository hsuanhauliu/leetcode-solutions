"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """ BFS solution
        Time: O(n)
        Space: O(n)
        
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        counter = 0
        curr_level = [root]
        next_level = []
        
        while curr_level:
            counter += 1
            for n in curr_level:
                for c in n.children:
                    next_level.append(c)
            curr_level = next_level
            next_level = []
        
        return counter