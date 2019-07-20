class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """ DP solution.
        Similar to coin change problem, we want to find the number of ways
        to make up numbers from 1 to target.
        
        Time: O(n)
        Space: O(n)
        """
        if not nums:
            return 0
        
        nums = sorted(nums)
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for n in nums:
                if n > i:
                    break
                dp[i] += dp[i - n]
        
        return dp[-1]
        
        
    def combinationSum42(self, nums: List[int], target: int) -> int:
        """ Brute force. Try every combination. """
        def find_sum(curr):
            if not curr:
                return 1
            
            res = 0
            for n in nums:
                if curr >= n:
                    res += find_sum(curr - n)
            return res
        
        return find_sum(target)