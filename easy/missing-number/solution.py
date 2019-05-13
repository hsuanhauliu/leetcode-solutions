class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i, n in enumerate(nums):
            if i != n:
                return i
        return len(nums)
    
    def missingNumber2(self, nums2):
        """ 
        A very clever solution posted on the Discussion forum.

        Basically, we calculate the sum from 0 to n WITHOUT missing numbers, by
        doing n * (n+1) / 2. Then, we subtract the sum of all elements that we
        actually have. The resulting number is the number that is missing.
        """
        n = len(nums2)
        return n * (n + 1) / 2 - sum(nums2)