class Solution:
    def longestMountain(self, a: List[int]) -> int:
        head = tail = n = len(a)
        longest = 0
        for i in range(1, n):
            if a[i-1] < a[i]:
                head = i - 1
                tail = i
                break
                
        increasing = True
        while tail < n:
            if increasing:
                if a[tail-1] == a[tail]:
                    head = tail
                elif a[tail-1] > a[tail]:
                    if tail - head < 2:
                        head = tail
                    else:
                        increasing = False
                    
            if not increasing:
                if a[tail-1] > a[tail]:
                    longest = max(longest, tail - head + 1)
                elif a[tail-1] <= a[tail]:
                    increasing = True
                    longest = max(longest, tail - head)
                    head = tail
                    if a[tail-1] < a[tail]:
                        head -= 1
                    
            tail += 1
        return longest