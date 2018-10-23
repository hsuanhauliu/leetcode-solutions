class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None
        self.leftTreeCount = 0

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val, root):
        if not root:
            self.root = Node(val)
            return 0

        if val == root.val:
            root.count += 1
            return root.leftTreeCount
    
        if val < root.val:
            root.leftTreeCount += 1
            if not root.left:
                root.left = Node(val)
                return 0
            return self.add(val, root.left)

        if not root.right:
            root.right = Node(val)
            return root.count + root.leftTreeCount

        return root.count + root.leftTreeCount + self.add(val, root.right)

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tree = BinaryTree()

        return [tree.add(n, tree.root) for n in reversed(nums)][::-1]
