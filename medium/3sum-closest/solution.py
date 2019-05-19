class Solution(object):
    def threeSumClosest(self, nums, target):
        """ Optimized solution
        First sort the list in ascending order and use two pointers to narrow down search.
        
        Time: O(n^2)
        Space: O(n) * if we sort the list in-place, this would be O(1)
        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sorted_nums = sorted(nums)
        length = len(nums)
        closest = float('inf')
        for a in range(length - 2):
            b = a + 1
            c = length - 1
            while b < c:
                s = sorted_nums[a] + sorted_nums[b] + sorted_nums[c]
                if s == target:
                    return s
                
                if abs(target - s) < abs(target - closest):
                    closest = s
                
                if s < target:
                    b += 1
                else:
                    c -= 1
                    
        return closest
        
    def threeSumClosest2(self, nums, target):
        """ Brute force solution
        Time: O(n^3)
        Space: O(1)
        """
        length = len(nums)
        closest = float('inf')
        for a in range(length):
            for b in range(a + 1, length):
                for c in range(b + 1, length):
                    s = nums[a] + nums[b] + nums[c]
                    if abs(target - s) < abs(target - closest):
                        closest = s
        return closest