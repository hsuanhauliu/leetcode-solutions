class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr, res = 1, 0
        for i in range(1, len(nums)):
            curr = curr + 1 if nums[i-1] < nums[i] else 1
            res = max(res, curr)
        return 1 if len(nums) == 1 else res
