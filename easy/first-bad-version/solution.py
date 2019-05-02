# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        h = 1
        while h != n:
            m = (h + n) // 2
            if isBadVersion(m):
                n = m
            else:
                h = m + 1

        return h
