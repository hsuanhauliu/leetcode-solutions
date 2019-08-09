import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """ Use min-heap to grab the next ugly number.
        Time: O(nlogn)
        Space: O(n)
        """
        candidates = []
        ugly_nums = set()
        counter = curr = 1
        while counter < n:
            counter += 1
            for factor in [2, 3, 5]:
                next_num = curr * factor
                if next_num not in ugly_nums:
                    heapq.heappush(candidates, next_num)
                    ugly_nums.add(next_num)
            curr = heapq.heappop(candidates)
        return curr
        
        
    def nthUglyNumber2(self, n: int) -> int:
        """ Check every number to see if it is ugly.
        TLE
        """
        def is_ugly(num, ugly_nums):
            for factor in [2, 3, 5]:
                if not (num % factor) and (num // factor) in ugly_nums:
                    return True
            return False
        
        ugly_nums = set([1])
        counter = curr = 1
        while counter < n:
            curr += 1
            if is_ugly(curr, ugly_nums):
                counter += 1
                ugly_nums.add(curr)
        return curr