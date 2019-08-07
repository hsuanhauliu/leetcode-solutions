class Solution:
    def sortArrayByParityII(self, a: List[int]) -> List[int]:
        """ Two pointers. Find numbers that are out of place and swap.
        Time: O(n)
        Space: O(1)
        """
        even_i, odd_i, size = 0, 1, len(a)
        while even_i < size and odd_i < size:
            
            while even_i < size and a[even_i] % 2 == 0:
                even_i += 2
            
            while odd_i < size and a[odd_i] % 2 == 1:
                odd_i += 2
                
            if even_i < size:
                a[even_i], a[odd_i] = a[odd_i], a[even_i]
                even_i += 2
                odd_i += 2
        
        return a