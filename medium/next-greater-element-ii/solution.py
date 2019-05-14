class Solution(object):
    def nextGreaterElements(self, nums):
        """ Stack solution O(n)
        :type nums: List[int]
        :rtype: List[int]
        """
        my_stack = []
        length = len(nums)
        res = [-1] * length

        for i in range(length):
            while my_stack and nums[my_stack[-1]] < nums[i]:
                res[my_stack.pop()] = nums[i]
            my_stack.append(i)

        for i in range(length):
            while my_stack and nums[my_stack[-1]] < nums[i]:
                res[my_stack.pop()] = nums[i]
            if not my_stack:
                break

        return res

 
    def nextGreaterElements2(self, nums):
        """ Naive solution O(n^2)
        :type nums: List[int]
        :rtype: List[int]
        """
        def find_next_element(self, nums, i, target):
            """ Helper function """
        for n in nums[i+1:] + nums[:i]:
            if n > target:
                return n
        return -1
    
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = self.find_next_element(nums, i, nums[i])
        return res
