class Solution:
    def lenLongestFibSubseq(self, a: List[int]) -> int:
        """ Count all pairs and use table to keep track of length of sequence
        end with a[i], a[j].
        
        Time: O(n^2)
        Space: O(n^2)
        """
        nums = set(a)
        size = len(a)
        dp = {}
        longest = 0
        for i in range(size-1):
            for j in range(1, size):
                second, third = a[i], a[j]
                first = third - second
                if first in nums and first < second:
                    if (first, second) in dp:
                        dp[(second, third)] = dp[(first, second)] + 1
                    else:
                        dp[(second, third)] = 3
                    longest = max(longest, dp[(second, third)])
        return longest