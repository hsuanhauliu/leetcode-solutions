class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        curr_max = prices[-1]
        curr_profit = 0
        for i in reversed(range(n - 1)):
            curr_profit = max(curr_profit, curr_max - prices[i])
            curr_max = max(curr_max, prices[i])
            
        return curr_profit