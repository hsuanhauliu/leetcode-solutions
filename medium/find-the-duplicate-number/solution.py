class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ Detect cycle and entry point """
        slow = nums[0]
        fast = nums[slow]
        
        # find meeting point
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # now find entry point
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow