# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.nodes = []
        self._flatten(root)
        self.curr = 0
        self.limit = len(self.nodes)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.curr += 1
        return self.nodes[self.curr - 1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curr < self.limit
    
    def _flatten(self, root):
        if root:
            self._flatten(root.left)
            self.nodes.append(root.val)
            self._flatten(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()