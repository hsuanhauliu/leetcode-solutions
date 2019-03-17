class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        curr = nums[0]
        maximum = nums[0]

        for n in nums[1:]:
            curr = max(n, curr + n)
            maximum = max(maximum, curr)

        return maximum
