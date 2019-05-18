class Solution(object):
    def fib(self, n):
        """ Basic recursion implementation
        :type N: int
        :rtype: int
        """
        # base cases
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)
    
    def fib2(self, n):
        """ Optimize with a lookup table.
        
        """
        if n < 2:
            return n
        
        lookup_table = [-1] * (n + 1)
        lookup_table[0] = 0
        lookup_table[1] = 1
        
        def helper(n, t):
            if t[n] == -1:
                t[n] = helper(n-1, t) + helper(n-2, t)
            return t[n]
        
        helper(n, lookup_table)
        return lookup_table[-1]