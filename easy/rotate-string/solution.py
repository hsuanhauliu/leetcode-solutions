class Solution:
    def rotateString(self, a: str, b: str) -> bool:
        """ Brute-force: check if b is in the extended string of a
        
        Time: O(n^2)
        Space: O(n)
        """
        len_a = len(a)
        len_b = len(b)
        if len_a == len_b:
            if not a:
                return True
            
            check_str = a + a[:-1]
            for i in range(len_a):
                if check_str[i:i + len_a] == b:
                    return True
                
        return False