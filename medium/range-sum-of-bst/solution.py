#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, l, r):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        if not root:
            return 0

        if root.val > r:
            return self.rangeSumBST(root.left, l, r)

        if root.val < l:
            return self.rangeSumBST(root.right, l, r)

        return root.val + self.rangeSumBST(root.left, l, r) + self.rangeSumBST(root.right, l, r)


def main():
    sol = Solution()

    r = TreeNode(10)
    r.left = TreeNode(5)
    r.left.left = TreeNode(3)
    r.left.right = TreeNode(7)
    r.right = TreeNode(15)
    r.right.right = TreeNode(18)

    print(sol.rangeSumBST(r, 7, 15))
    print(sol.rangeSumBST(None, 7, 15))
    print(sol.rangeSumBST(r, 18, 20))
    print(sol.rangeSumBST(r, 19, 20))


if __name__ == "__main__":
    main()
