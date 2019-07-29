class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """ Reverse solution. Reverse the first n-k and remaining k
        elements separately, then reverse the whole array.
        
        Time: O(n)
        Space: O(1)
        """
        if not nums:
            return
        
        size = len(nums)
        k = k % size
        if not k:
            return
        
        remain = size - k
        for i in range(remain // 2):
            nums[i], nums[remain-1-i] = nums[remain-1-i], nums[i]
        
        for i in range(k // 2):
            nums[i+remain], nums[size-1-i] = nums[size-1-i], nums[i+remain]
        
        for i in range(size // 2):
            nums[i], nums[size-1-i] = nums[size-1-i], nums[i]
        
        
    def rotate2(self, nums: List[int], k: int) -> None:
        """ Cache the first size - k numbers and replace elements
        one by one.
        
        Time: O(n)
        Space: O(n)
        """
        if not nums:
            return
        
        # if the shift is pointless
        size = len(nums)
        k = k % size
        if not k:
            return
        
        shift_left = size - k
        temp = nums[:shift_left]
        # shift the first shift_left elements
        for i in range(shift_left, size):
            nums[(i + k) % size] = nums[i]
        
        # copy over the rest
        for i in range(shift_left):
            nums[i + k] = temp[i]