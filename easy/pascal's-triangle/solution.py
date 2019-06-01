class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """ DP solution
        Allocate a triangle full of 1's and calculate number for each row.
        
        Time: O(n^2)
        Space: O(n^2)
        """
        res = [[1] * (i + 1) for i in range(numRows)]
        for i in range(1, numRows - 1):
            for j in range(1, i + 1):
                res[i + 1][j] = res[i][j - 1] + res[i][j]
                
        return res
        
        
    def generate2(self, numRows: int) -> List[List[int]]:
        """ Brute-force solution
        Generate all rows and insert to final result.
        
        Time: O(n^2)
        Space: O(n^2)
        """
        if not numRows:
            return []
        
        res = [[1]]
        for i in range(2, numRows + 1):
            row = [1]
            prev = res[-1]
            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            res.append(row)
            
        return res
