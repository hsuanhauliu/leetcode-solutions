class Solution:
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        """ DP solution.
        
        Time: O(n * m)
        Space: O(n * m)
        """
        len_a, len_b = len(a) + 1, len(b) + 1
        dp = [[0] * len_b for _ in range(len_a)]
        for row in range(1, len_a):
            for col in range(1, len_b):
                if a[row-1] == b[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        return dp[-1][-1]