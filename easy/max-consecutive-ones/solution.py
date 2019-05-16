class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones = 0
        last = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                max_ones = max(max_ones, i - last - 1)
                last = i
                
        return max(max_ones, len(nums) - last - 1)