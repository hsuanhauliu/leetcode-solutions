class Solution:
    def numberOfArithmeticSlices(self, a: List[int]) -> int:
        start = res = 0
        size = len(a)
        while start <= size - 3:
            gap = a[start + 1] - a[start]
            curr = start + 1
            while curr + 1 < size and a[curr + 1] - a[curr] == gap:
                curr += 1
            
            length = curr - start + 1
            if length > 2:
                n = length - 3 + 1
                res += n * (n + 1) // 2
            
            start = curr
        
        return res
                