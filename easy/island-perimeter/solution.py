class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        perimeters = 0
        connected = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if not connected:
                        perimeters += 1
                        connected = True
                else:
                    connected = False
            connected = False

        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j]:
                    if not connected:
                        perimeters += 1
                        connected = True
                else:
                    connected = False
            connected = False

        return perimeters * 2

sol = Solution()
print(sol.islandPerimeter([[0,1,0,1],
                     [1,1,1,1],
                     [0,1,0,1],
                     [1,1,0,1]]))
