class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        size = len(a)
        dp = a[0][:]
        
        for i in range(1, size):
            prev_dp = dp[:]
            for j in range(size):
                dp[j] = a[i][j] + min(prev_dp[col] for col in self.location_above(j, size))
        
        return min(dp)
    
    
    def location_above(self, curr, limit):
        res = []
        if curr > 0:
            res.append(curr - 1)
        res.append(curr)
        if curr + 1 < limit:
            res.append(curr + 1)
        return res