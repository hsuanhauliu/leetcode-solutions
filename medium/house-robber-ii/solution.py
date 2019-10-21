class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        def helper(sub_nums):
            dp = [0] * len(sub_nums)
            dp[0] = sub_nums[0]
            dp[1] = max(sub_nums[0], sub_nums[1])

            for i in range(2, len(sub_nums)):
                dp[i] = max(sub_nums[i] + dp[i-2], dp[i-1])

            return dp[-1]
        
        return max(helper(nums[:-1]), helper(nums[1:]))
    
        