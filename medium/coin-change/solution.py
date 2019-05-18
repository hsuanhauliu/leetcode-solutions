class Solution(object):
    def coinChange(self, coins, amount):
        """ Standard DP solution
        
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        return -1 if dp[-1] > amount else dp[-1]