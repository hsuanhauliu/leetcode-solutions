class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ Merge sort """
        length = len(nums)
        if length < 2:
            return nums
        
        l = self.sortArray(nums[:length // 2])
        r = self.sortArray(nums[length // 2:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        res = []
        while l and r:
            if l[0] < r[0]:
                res.append(l.pop(0))
            else:
                res.append(r.pop(0))
        
        if l:
            res += l
        if r:
            res += r
            
        return res