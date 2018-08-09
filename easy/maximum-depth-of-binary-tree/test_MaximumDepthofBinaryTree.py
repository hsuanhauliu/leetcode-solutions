import unittest
import MaximumDepthofBinaryTree as mdbt


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


sol = mdbt.Solution()


class TestMaximumDepth(unittest.TestCase):

    def test_MaxDepth(self):
        self.assertEqual(0, sol.maxDepth(None))

        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertEqual(3, sol.maxDepth(root1))


if __name__ == '__main__':
    unittest.main()
