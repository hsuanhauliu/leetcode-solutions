class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
            res += matrix[0]            # append first row to result
            matrix = matrix[1:]         # take out the first row
            matrix = zip(*matrix)[::-1] # rotate counter-clockwise 90 degrees
            
        return res