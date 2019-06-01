class Solution:
    def maxRotateFunction(self, a: List[int]) -> int:
        """ Math solution
        f(n + 1) = f(n) - sum(a) + len(a) * a[n - 1]
        
        Time: O(n)
        Space: O(1)
        """
        length = len(a)
        total = sum(a)
        maximum = curr = sum(i * v for i, v in enumerate(a))
        for i in range(1, length):
            curr = curr - total + length * a[i - 1]
            maximum = max(maximum, curr)
        
        return maximum
        
    def maxRotateFunction2(self, a: List[int]) -> int:
        """ Brute-force solution
        Try every possible combination and calculate rotation.
        
        Time: O(n^2)
        Space: O(1)
        """
        def rotation(l):
            total = 0
            for i, v in enumerate(l):
                total += i * v
            return total
        
        def shift(l):
            temp = l.pop(-1)
            l.insert(0, temp)
        
        length = len(a)
        maximum = rotation(a)
        for _ in range(length):
            maximum = max(maximum, rotation(a))
            shift(a)
        
        return maximum