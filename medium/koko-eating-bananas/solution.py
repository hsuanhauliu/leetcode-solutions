import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        lower_bound = 1
        upper_bound = max(piles)

        while lower_bound < upper_bound:
            k = (lower_bound + upper_bound) // 2
            time = self.calculate_time(piles, k)
            if time > h:
                lower_bound = k + 1
            else:
                upper_bound = k
        return lower_bound


    def calculate_time(self, piles, k):
        return sum([math.ceil(bananas / k) for bananas in piles])
