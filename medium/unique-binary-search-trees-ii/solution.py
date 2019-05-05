# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.gen_trees(1, n)

    def gen_trees(self, h, t):
        trees = []
        for curr in range(h, t + 1):
            l = self.gen_trees(h, curr - 1)
            r = self.gen_trees(curr + 1, t)
            self.append_trees(trees, curr, l, r)
        return trees

    def append_trees(self, trees, v, l, r):
        if not l:
            l.append(None)
        if not r:
            r.append(None)
        for l_subtree in l:
            for r_subtree in r:
                new_root = TreeNode(v)
                new_root.left = l_subtree
                new_root.right = r_subtree
                trees.append(new_root)
