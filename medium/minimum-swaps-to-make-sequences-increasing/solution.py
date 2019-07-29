class Solution:
    def minSwap(self, a: List[int], b: List[int]) -> int:
        prev_a, prev_b, swap_1, swap_2 = a[0], b[0], 0, 1
        for i in range(1, len(a)):
            curr_a, curr_b = a[i], b[i]
            
            # don't swap
            next_swap_1 = swap_1
            if prev_b < curr_a and prev_a < curr_b:
                next_swap_1 = swap_2
                if prev_a < curr_a and prev_b < curr_b:
                    next_swap_1 = min(swap_1, swap_2)
            
            # swap
            next_swap_2 = swap_2 + 1
            if prev_a < curr_b and prev_b < curr_a:
                next_swap_2 = swap_1 + 1
                if prev_b < curr_b and prev_a < curr_a:
                    next_swap_2 = min(swap_1 + 1, swap_2 + 1)
                    
            prev_a, prev_b, swap_1, swap_2 = a[i], b[i], next_swap_1, next_swap_2
        
        return min(swap_1, swap_2)