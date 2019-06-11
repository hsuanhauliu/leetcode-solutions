class Solution:
    def numTrees(self, n: int) -> int:
        """ Recursion with look-up table """
        if n < 2:
            return 1
        lookup_table = [-1] * (n + 1)
        lookup_table[0] = lookup_table [1] = 1
        return self.helper(n, lookup_table)
        
    def helper(self, n, table):
        if table[n] != -1:
            return table[n]
        
        res = 0
        for i in range(n):
            table[i] = self.helper(i, table)
            table[n-i-1] = self.helper(n-i-1, table)
            res += table[i] * table[n-i-1]
        return res
    
    
    
    def numTrees2(self, n: int) -> int:
        """ Straightforward recursion implementation """
        if n < 2:
            return 1
        
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        return res