class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        res = [[0 if matrix[i][j] == '0' else 1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                res[i][j] = 0 if matrix[i][j] == '0' else 1 + min(res[i-1][j-1], res[i-1][j], res[i][j-1])
        
        return max(max(r) for r in res) ** 2