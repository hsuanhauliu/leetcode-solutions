class Solution:
    def maxSumAfterPartitioning(self, a: List[int], k: int) -> int:
        """ DP Solution
        
        Time: O(n*k)
        Space: O(n)
        """
        size = len(a) + 1
        dp = [0] * size
        for curr in range(1, size):
            end = min(curr, k)
            dp[curr] = max(dp[curr-j] + j * max(a[curr-j:curr]) for j in range(1, end+1))
                
        return dp[-1]