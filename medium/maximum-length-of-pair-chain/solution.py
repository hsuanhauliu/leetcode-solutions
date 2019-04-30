class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sorted_pairs = sorted(pairs, key=lambda p: p[1])
        counter = 1
        prev = sorted_pairs[0][1]
        for i, j in sorted_pairs[1:]:
            if prev < i:
                counter += 1
                prev = j

        return counter
