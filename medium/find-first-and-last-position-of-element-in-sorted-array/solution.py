import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left = bisect.bisect_left(nums, target)
        if left < len(nums) and nums[left] == target:
            right = bisect.bisect_left(nums, target+1)
            return [left, right-1]
        return [-1, -1]