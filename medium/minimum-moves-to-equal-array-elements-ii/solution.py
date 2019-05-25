class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        """ Match all heights to the median or the smaller median
        Time: O(n)
        Space: O(n)
        """
        sorted_nums = sorted(nums)
        median = sorted_nums[len(nums) // 2]
        return sum(abs(median - n) for n in nums)
    
    def minMoves2_2(self, nums: List[int]) -> int:
        """ Fancy one-liner"""
        return sum(abs(sorted(nums)[len(nums) // 2] - n) for n in nums)