class Solution(object):
    def hammingWeight_1(self, n):
        """
        :type n: int
        :rtype: int

        Straight forward bit shifting and counting solution.
        """
        count = 0

        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1

        return count


    def hammingWeight_2(self, n):
        """
        Use a trick to drop the last 1 bit one at a time with n & (n - 1).
        """
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count


    def hammingWeight_3(self, n):
        """
        Use Python's built-in functions to convert n to binary string then count 1.
        """
        return bin(n).count('1')
