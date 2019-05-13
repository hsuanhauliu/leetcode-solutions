import heapq

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)

        mins = nums[:3]
        heapq.heapify(mins)

        for n in nums[3:]:
            if n > mins[0]:
                heapq.heapreplace(mins, n)

        return mins[0]
