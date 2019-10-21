class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n != 1:
            # keep dividing
            if n % 2:
                return False
            n //= 2
            
        return True