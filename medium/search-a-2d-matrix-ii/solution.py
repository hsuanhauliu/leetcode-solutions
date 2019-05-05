class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix[0]):
            return False
        
        r = 0
        c = len(matrix[0]) - 1
        while c >= 0 and r < len(matrix) - 1:
            print(r, c)
            if matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else:
                return True
        return False
