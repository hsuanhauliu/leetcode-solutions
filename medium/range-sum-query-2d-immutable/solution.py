class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self._calc_presum(matrix)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.presum[row1-1][col2] if row1 else 0
        b = self.presum[row2][col1-1] if col1 else 0
        c = self.presum[row1-1][col1-1] if row1 and col1 else 0
        return self.presum[row2][col2] - a - b + c
    
    
    def _calc_presum(self, matrix):
        for i in range(len(matrix)):
            row_sum = 0
            for j in range(len(matrix[0])):
                row_sum += matrix[i][j]
                self.presum[i][j] = row_sum + self.presum[i-1][j] if i else row_sum
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)