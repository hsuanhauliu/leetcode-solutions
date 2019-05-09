from collections import Counter

class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        counts = Counter(ages)
        total_requests = 0

        for b in counts:
            for a in counts:
                if a * 0.5 + 7 < b and b <= a:
                    if a == b:
                        total_requests += counts[a] * (counts[b] - 1)
                    else:
                        total_requests += counts[a] * counts[b]

        return total_requests

