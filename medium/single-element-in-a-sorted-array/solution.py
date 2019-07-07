class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """ Binary search """
        s, t = 0, len(nums) - 1
        while s < t:
            m1 = m2 = (s + t) // 2
            if m1 % 2 == 0:
                m2 += 1
            else:
                m1 -= 1
            
            if nums[m1] == nums[m2]:
                s = m2 + 1
            else:
                t = m1
                
        return nums[s]