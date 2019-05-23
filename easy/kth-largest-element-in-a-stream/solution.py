class KthLargest(object):
    """ Quick and dirty linear search insertion.
    Always keep the largest k elements to reduce insertion time.
    
    Time: construction time: O(NlgN), add time: O(K)
    Space: construction time: O(N), add time: O(1)
    """
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums)[-k:]
        
    def insert(self, val):
        last = len(self.nums)
        for i, v in enumerate(self.nums):
            if v >= val:
                last = i
                break
                
        self.nums.insert(last, val)
        if len(self.nums) > self.k:
            self.nums.pop(0)
        return
        
    def add(self, val):
        self.insert(val)
        return self.nums[0]