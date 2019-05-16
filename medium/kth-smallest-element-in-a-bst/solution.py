# Definition for a binary tree node.
#class TreeNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
        
class Solution(object):
    def kthSmallest(self, root, k):
        """ DFS approach
        Use a counter to count how many nodes we have visited. Once we reach k, we stop.
        
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def visit(node, curr):
            if not node:
                return (False, curr)
            
            l = visit(node.left, curr)
            
            # stop early so we don't have to search right subtree
            if l[0]:
                return l
            
            # count the current node
            curr = l[1] + 1
            if curr == k:
                return (True, node.val)
            
            # traverse down the right subtree
            return visit(node.right, curr)
        
        return visit(root, 0)[1]
        
        
    def kthSmallest2(self, root, k):
        """ Naive solution
        Find all elements and place them in a list. The kth element is the target.
        Time complexity: O(n^2) since appending lists take time too.
        Space complexity: O(n) there are only n elements in the list.
        """
        def getAllElements(node):
            if not node:
                return []
            left = getAllElements(node.left)
            left.append(node.val)
            right = getAllElements(node.right)
            return left + right
        
        return getAllElements(root)[k-1]