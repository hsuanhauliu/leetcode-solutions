class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        buckets = [[] for _ in range(m + n + 1)]
        for r in range(m):
            for c in range(n):
                buckets[r+c].append(matrix[r][c])
        
        res = []
        flip = True
        for b in buckets:
            if flip:
                for num in reversed(b):
                    res.append(num)
            else:
                for num in b:
                    res.append(num)
            flip = not flip
        
        return res