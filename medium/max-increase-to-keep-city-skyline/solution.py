class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """ More readable version.
        Find the tallest building height for each row and column,
        then increase the heights of other buildings to those limits.
        
        Time: O(n^2)
        Space: O(n)
        
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        total = 0
        r_size = len(grid)
        c_size = len(grid[0])
        r_limit = [0] * r_size
        c_limit = [0] * c_size
        
        for r in range(r_size):
            for c in range(c_size):
                height = grid[r][c]
                r_limit[r] = max(r_limit[r], height)
                c_limit[c] = max(c_limit[c], height)
        
        for r in range(r_size):
            for c in range(c_size):
                total += min(r_limit[r], c_limit[c]) - grid[r][c]
        
        return total
    
    def maxIncreaseKeepingSkyline2(self, grid):
        """ Compact version
        Note that in the description, we assume the grid is a square.
        
        Time: O(n^2)
        Space: O(n)
        """
        n = len(grid)
        r_limit = [max(row) for row in grid]
        c_limit = [max(grid[r][c] for r in range(n)) for c in range(n)]
        return sum(min(r_limit[r], c_limit[c]) - grid[r][c] for c in range(n) for r in range(n))