class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        
        diff = 1
        while diff < n:
            i, j = 0, diff
            while j < n:
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                i += 1
                j += 1
            diff += 1
        
        return dp[0][-1]