# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        if root:
            current_path = str(root.val)
            if not root.left and not root.right:
                res.append(current_path)
            else:
                self.find_all_paths(root.left, current_path, res)
                self.find_all_paths(root.right, current_path, res)
        return res
    
    def find_all_paths(self, root, current_path, all_paths):
        if not root:
            return
        
        current_path = current_path + "->" + str(root.val)
        if not root.left and not root.right:
            all_paths.append(current_path)
            return
        
        self.find_all_paths(root.left, current_path, all_paths)
        self.find_all_paths(root.right, current_path, all_paths)