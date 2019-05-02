class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_peak(0, len(nums) - 1, nums)

    def find_peak(self, h, t, nums):
        if h == t:
            return h

        m = (h + t) // 2
        if nums[m] > nums[m + 1]:
            return self.find_peak(h, m, nums)
        return self.find_peak(m + 1, t, nums)
