class Solution:
    def minPathSum(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        height = len(grid)
        width = len(grid[0])
        dp = [[0] * width for i in range(height)]
        dp[0][0] = grid[0][0]

        for i in range(1, height):
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, width):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        for i in range(1, height):
            for j in range(1, width):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[height - 1][width - 1]


def main():
    sol = Solution()

    # normal cases
    print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7)
    print(sol.minPathSum([[1, 3, 1], [1, 1, 1], [4, 2, 1]]) == 5)

    # edge cases
    print(sol.minPathSum([[]]) == 0)
    print(sol.minPathSum([[0]]) == 0)
    print(sol.minPathSum([[10]]) == 10)


if __name__ == '__main__':
    main()
