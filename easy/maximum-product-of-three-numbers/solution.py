class Solution:
    def maximumProduct1(self, nums: List[int]) -> int:
        """ Sort then compare two candidates. Since negative numbers can
        appear in the input, we can choose two negative numbers or none
        at all. Thus, the finally answer is the product of either the
        three largest numbers or the largest number multiply by the two
        smallest number.
        
        Time: O(nlogn)
        Space: O(n); O(1) if the sorting is done in-place
        """
        s_nums = sorted(nums, reverse=True)
        return max(s_nums[0] * s_nums[1] * s_nums[2], s_nums[0] * s_nums[-1] * s_nums[-2])
    
    
    def maximumProduct2(self, nums: List[int]) -> int:
        """ Simply find the three largest numbers and two smallest numbers
        and compare them.
        
        Time: O(n)
        Space: O(1)
        """
        big_1 = big_2 = big_3 = -float("inf")
        small_1 = small_2 = float("inf")
        for n in nums:
            if n >= big_1:
                big_1, big_2, big_3 = n, big_1, big_2
            elif n >= big_2:
                big_2, big_3 = n, big_2
            elif n >= big_3:
                big_3 = n
            
            if n <= small_1:
                small_1, small_2 = n, small_1
            elif n <= small_2:
                small_2 = n
        
        return max(big_1 * big_2 * big_3, big_1 * small_1 * small_2)