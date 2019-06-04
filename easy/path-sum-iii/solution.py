# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.countPaths(root, sum, [])
    
    def countPaths(self, root, sum, curr_paths):
        if not root:
            return 0
        
        counter = 1 if root.val == sum else 0
        new_paths = [root.val]
        for s in curr_paths:
            new_sum = root.val + s
            new_paths.append(new_sum)
            if new_sum == sum:
                counter += 1
        
        return counter + self.countPaths(root.left, sum, new_paths) + self.countPaths(root.right, sum, new_paths)