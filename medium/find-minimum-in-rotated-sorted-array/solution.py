class Solution:
    def findMin(self, nums: List[int]) -> int:
        """ Linear search from the back
        Time: O(n)
        Space: O(1)
        """
        minimum = nums[0]
        for i in reversed(range(len(nums))):
            if nums[i] < minimum:
                minimum = nums[i]
            else:
                return minimum
        return minimum