class Solution:
    def tribonacci(self, n: int) -> int:
        """ Recursive DFS with memoization
        Time: O(n)
        Space: O(n)
        """
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        return self.dfs(n, dp)
    
    def dfs(self, n, dp):
        if n < 3 or dp[n]:
            return dp[n]
        
        dp[n] = self.dfs(n-1, dp) + self.dfs(n-2, dp) + self.dfs(n-3, dp)
        return dp[n]