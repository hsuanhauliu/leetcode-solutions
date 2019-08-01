# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        """ Compare numbers in in-order traversal.
        Time: O(n)
        Space: O(1)
        """
        prev = [-float('inf')]
        curr_min = [float('inf')]
        def inorder_traverse(node, prev, curr_min):
            if node:
                inorder_traverse(node.left, prev, curr_min)
                curr_min[0] = min(curr_min[0], node.val - prev[0])
                prev[0] = node.val
                inorder_traverse(node.right, prev, curr_min)
                
        inorder_traverse(root, prev, curr_min)
        return curr_min[0]
    
    
    def minDiffInBST2(self, root: TreeNode) -> int:
        """ Flatten tree then find minimum diff.
        
        Time: O(n)
        Space: O(n)
        """
        def flatten(node, all_nodes):
            if node:
                flatten(node.left, all_nodes)
                all_nodes.append(node.val)
                flatten(node.right, all_nodes)
            
        nodes = []
        flatten(root, nodes)
        diff = nodes[1] - nodes[0]
        for i in range(2, len(nodes)):
            diff = min(diff, nodes[i] - nodes[i-1])
        return diff
        