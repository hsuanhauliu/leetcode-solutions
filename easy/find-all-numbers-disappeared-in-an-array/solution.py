class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """ Swap numbers to be at their correct indices. 
        Time: O(n)
        Space: O(1) excluding output list
        """
        i, n, res = 0, len(nums), []
        while i < n:
            if nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
            else:
                i += 1
        
        for i, num in enumerate(nums):
            if i + 1 != num:
                res.append(i + 1)
                
        return res
        
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        """ Sort and add numbers that aren't in nums.
        Time: O(nlogn)
        Space: O(1) excluding output list
        """
        nums.sort()
        res = []
        curr, i, n = 1, 0, len(nums)
        while i < n:
            if curr < nums[i]:
                res.append(curr)
                curr += 1
            elif curr > nums[i]:
                i += 1
            else:
                curr += 1
                i += 1
        
        while curr < n + 1:
            res.append(curr)
            curr += 1
        return res
    
    def findDisappearedNumbers3(self, nums: List[int]) -> List[int]:
        """ Subtract numbers seen from set of numbers from 1 to n.
        Time: O(n)
        Space: O(n)
        """
        all_nums = set(n for n in range(1, len(nums) + 1))
        seen = set(n for n in nums)
        return list(all_nums - seen)