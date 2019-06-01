class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        length = len(nums)
        prev = None
        for i in range(length):
            if prev == None:
                prev = nums[i]
            elif nums[i - 1] != nums[i] - 1:
                if prev == nums[i - 1]:
                    res.append(str(prev))
                else:
                    res.append(str(prev) + "->" + str(nums[i - 1]))
                prev = nums[i]
        
        if prev == nums[-1]:
            res.append(str(prev))
        else:
            res.append(str(prev) + "->" + str(nums[-1]))
            
        return res