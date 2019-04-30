# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            root = new_root
        else:
            queue = [root]
            for _ in range(d - 2):
                queue = [child for node in queue for child in (node.left, node.right) if child]

            for node in queue:
                new_left_node, new_right_node = TreeNode(v), TreeNode(v)
                new_left_node.left, new_right_node.right = node.left, node.right
                node.left, node.right = new_left_node, new_right_node
        return root
