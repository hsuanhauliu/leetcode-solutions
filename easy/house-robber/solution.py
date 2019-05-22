class Solution:
    def rob(self, nums: List[int]) -> int:
        """ DP approach with one array.
        
        """
        length = len(nums)
        if not nums:
            return 0
        
        if length == 1:
            return nums[0]
        
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, length):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]