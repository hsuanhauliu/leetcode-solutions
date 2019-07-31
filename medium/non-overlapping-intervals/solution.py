class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ Formulate this problem as maximizing the number of intervals
        first and then the minimum number of intervals to be removed will
        be total length - max.
        
        Time: O(nlogn)
        Space: O(n) due to sorting. If we do it in-place this would be O(1)
        """
        count, last, size = 0, -float('inf'), len(intervals)
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if last <= start:
                count += 1
                last = end
        return size - count