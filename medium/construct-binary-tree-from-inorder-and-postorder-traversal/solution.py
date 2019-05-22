# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """ Recursion reversed-pos-order traversal.
        Traverse in reversed-pos-order allows us to construct the tree in the
        order of root, right, left, so we will be able to construct the tree
        from top to bottom. Given the root node, we can split the in-order
        list to two lists. The left list contains all elements in the left
        subtree and the right list contains all elements in the right subtree.
        
        Time: O(n)
        Space: O(n)
        """
        def construct(ino, pos):
            if not ino:
                return None
            
            root = TreeNode(pos.pop())
            split = ino.index(root.val)
            root.right = construct(ino[split+1:], pos)
            root.left = construct(ino[:split], pos)
            return root
        
        return construct(inorder[:], postorder[:])