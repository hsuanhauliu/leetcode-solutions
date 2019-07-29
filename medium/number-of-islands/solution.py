class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ DFS approach.
        Time: O(n)
        Space: O(n)
        """
        if not grid or not grid[0]:
            return 0
        
        size_r = len(grid)
        size_c = len(grid[0])
        counts = 0
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            if grid[r][c] == '0':
                return 0
            
            for n_r, n_c in get_moves(r, c):
                dfs(n_r, n_c)
            return 1
            
        def get_moves(r, c):
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            res = []
            for d_r, d_c in dirs:
                n_r, n_c = r + d_r, c + d_c
                if n_r >= 0 and n_r < size_r and n_c >= 0 and n_c < size_c:
                    res.append((n_r, n_c))
            return res
        
        for row in range(size_r):
            for col in range(size_c):
                counts += dfs(row, col)
        return counts