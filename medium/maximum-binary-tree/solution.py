# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            max_i, max_v = max(enumerate(nums), key=lambda x: x[1])
            root = TreeNode(max_v)
            root.left = self.constructMaximumBinaryTree(nums[:max_i])
            root.right = self.constructMaximumBinaryTree(nums[max_i + 1:])
            return root
        return None