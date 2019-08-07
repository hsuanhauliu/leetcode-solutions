class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if sum(nums) % 2:
            return False
        
        target = total // 2
        checked = set()
        return self.find_sum(target, sorted(nums, reverse=True), 0, checked)
    
    
    def find_sum(self, target, nums, start, checked):
        if not target:
            return True
        
        if target in checked:
            return False
        
        for i in range(start, len(nums)):
            curr = nums[i]
            if target >= curr and self.find_sum(target-curr, nums, i+1, checked):
                return True
        
        # if we know there is no way to make up this number
        checked.add(target)
        return False