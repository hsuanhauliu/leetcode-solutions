class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """ Two Pointers Solution
        Time: O(n)
        Space: O(1)
        """
        if k <= min(nums):
            return 0
        
        length = len(nums)
        head = tail = counter = 0
        product = 1
        while tail < length and head < length:
            if nums[tail] >= k:
                counter += (tail - head) * (tail - head + 1) // 2
                product = 1
                head = tail = tail + 1
            elif product * nums[tail] < k:
                product *= nums[tail]
                tail += 1
            else:
                counter += tail - head
                product //= nums[head]
                head += 1
                
        return counter + (length - head) * (length - head + 1) // 2