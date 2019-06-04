class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ Use recursion to find all combinations.
        Time: O(n^2)
        Space: O(n^2)
        """
        res = [[]]
        if not nums:
            return res
        return res + self.findAllSubsets(nums)
    
    def findAllSubsets(self, nums):
        if len(nums) == 1:
            return [nums]
        
        curr = [nums[0]]
        subsets = self.findAllSubsets(nums[1:])
        res = [curr] + [curr + sub for sub in subsets]
        subsets.extend(res)
        return subsets