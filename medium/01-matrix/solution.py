class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        """ DP solution """
        max_d = 10000
        res = [[0 if not num else max_d for num in row] for row in matrix]
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if res[r][c]:
                    cell_u = cell_l = max_d
                    if -1 < r - 1:
                        cell_u = res[r-1][c]
                    if -1 < c - 1:
                        cell_l = res[r][c-1]
                    res[r][c] = 1 + min(cell_u, cell_l)
                    
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if res[r][c]:
                    cell_d = cell_r = max_d
                    if r + 1 < rows:
                        cell_d = res[r+1][c]
                    if c + 1 < cols:
                        cell_r = res[r][c+1]
                    res[r][c] = min(1 + min(cell_d, cell_r), res[r][c])
                
        return res
        
        
    def updateMatrix2(self, matrix: List[List[int]]) -> List[List[int]]:
        """ BFS solution """
        res = [[0 if not num else 10000 for num in row] for row in matrix]
        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(rows):
            for c in range(cols):
                if not res[r][c]:
                    self._find_shortest_distance(r, c, res, rows, cols)
        
        return res
        
    
    def _find_shortest_distance(self, curr_r, curr_c, table, max_r, max_c):
        """ Perform bfs to find shortest distance to 0 """
        curr_level = [(curr_r, curr_c)]
        next_level = []
        distance = 0
        
        while curr_level:
            distance += 1
            for r, c in curr_level:
                for n_r, n_c in self._generate_neighbor(r, c, max_r, max_c):
                    if distance < table[n_r][n_c]:
                        table[n_r][n_c] = distance
                        next_level.append((n_r, n_c))
            
            curr_level = next_level
            next_level = []
    
    
    def _generate_neighbor(self, r, c, max_r, max_c):
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for m_r, m_c in moves:
            next_r = r + m_r
            next_c = c + m_c
            if -1 < next_r and next_r < max_r and -1 < next_c and next_c < max_c:
                yield (next_r, next_c)