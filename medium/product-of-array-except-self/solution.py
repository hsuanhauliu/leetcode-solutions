class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """ Two-pass approach
        One the first pass, use the list to record the product of all
        elements on the left side including the number itself. On the
        second pass, we traverse backward. The product excluding self
        would be all products on the left and right side. We can use a
        single variable to record the current product of all elements
        on the right side.
        
        Time: O(n)
        Space: O(1): excluding output space
        """
        length = len(nums)
        res = [1] * length
        res[0] = nums[0]
        for i in range(1, length - 1):
            res[i] = res[i-1] * nums[i]
        
        res[-1] = res[-2]
        right_product = nums[-1]
        for i in reversed(range(1, length - 1)):
            res[i] = res[i-1] * right_product
            right_product *= nums[i]
        
        res[0] = right_product
        return res