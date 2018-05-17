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
            #print "case 0"
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # determine range
        #print "case 1"
        mid = len(nums) / 2

        start_num = nums[0]
        end_num = nums[mid]

        if start_num < end_num:
            if start_num <= target and target < end_num:
                temp = self.search(nums[:mid], target)
                if temp == -1:
                    return -1
                return temp

            #print "case 2"
            temp = self.search(nums[mid:], target)
            if temp == -1:
                return -1
            return mid + temp

        if end_num <= target and target < start_num:
            temp = self.search(nums[mid:], target)
            if temp == -1:
                return -1
            return mid + temp

        temp = self.search(nums[:mid], target)
        if temp == -1:
            return -1
        return temp
