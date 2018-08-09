import unittest
import MinimumDepthofBinaryTree as mdbt


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


sol = mdbt.Solution()


class TestMinimumDepth(unittest.TestCase):

    def test_MinDepth(self):
        self.assertEqual(0, sol.minDepth(None))

        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertEqual(2, sol.minDepth(root1))

        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        self.assertEqual(2, sol.minDepth(root2))


if __name__ == '__main__':
    unittest.main()

