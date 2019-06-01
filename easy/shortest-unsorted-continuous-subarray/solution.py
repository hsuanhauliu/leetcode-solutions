class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """ Brute force
        Compare each element with the sorted version of nums.
        
        Time: O(nlogn)
        Space: O(n)
        """
        sorted_nums = sorted(nums)
        
        # find elements that are out of place
        h = 0
        while h < len(nums) and nums[h] == sorted_nums[h]:
            h += 1
            
            # if nothing is out of place
            if h == len(nums):
                return 0
        
        t = len(nums) - 1
        while t > 0 and nums[t] == sorted_nums[t]:
            t -= 1
            
        return t - h + 1