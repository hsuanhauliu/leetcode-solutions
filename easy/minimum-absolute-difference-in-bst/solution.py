# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """ In-order traversal to flatten tree and find minimum difference.
        Time: O(n)
        Space: O(n)
        """
        def flatten(curr_node, nodes):
            if not curr_node:
                return
            
            flatten(curr_node.left, nodes)
            nodes.append(curr_node.val)
            flatten(curr_node.right, nodes)
        
        flattened_tree = []
        flatten(root, flattened_tree)
        min_diff = flattened_tree[1] - flattened_tree[0]
        for i in range(2, len(flattened_tree)):
            min_diff = min(min_diff, flattened_tree[i] - flattened_tree[i-1])
        
        return min_diff