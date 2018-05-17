class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # base cases
        if len(nums) == 0:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # determine range
        mid = len(nums) / 2
        start_num = nums[0]
        mid_num = nums[mid]

        if start_num < mid_num:
            if start_num <= target and target < mid_num:
                return self.search(nums[:mid], target)

            temp = self.search(nums[mid:], target)
            if temp == -1:
                return -1
            return mid + temp

        if mid_num <= target and target < start_num:
            temp = self.search(nums[mid:], target)
            if temp == -1:
                return -1
            return mid + temp

        return self.search(nums[:mid], target)
