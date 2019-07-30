class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """ Two pointers approach. Move the non-zero number at
        position next_p to curr_p.
        
        Time: O(n)
        Space: O(1)
        """
        curr_p, next_p, size = 0, 0, len(nums)
        
        while next_p < size:
            if nums[next_p]:
                nums[curr_p] = nums[next_p]
                curr_p += 1
            next_p += 1
        
        while curr_p < size:
            nums[curr_p] = 0
            curr_p += 1