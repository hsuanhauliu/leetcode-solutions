class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """ Compare the top 2 max numbers.
        
        Time: O(n)
        Space: O(1)
        """
        max_1 = max_2 = i_1 = i_2 = -1
        for i, n in enumerate(nums):
            if n > max_1:
                max_1, max_2 = n, max_1
                i_1, i_2 = i, i_1
            elif n > max_2:
                max_2, i_2 = n, i
        
        return -1 if max_1 < max_2 * 2 else i_1