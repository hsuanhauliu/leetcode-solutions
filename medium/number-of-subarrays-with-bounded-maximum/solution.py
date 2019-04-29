class Solution(object):
    def numSubarrayBoundedMax(self, a, l, r):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        total = 0
        curr = 0
        head = -1

        for i in range(len(a)):
            if a[i] < l:
                total += curr
            elif a[i] > r:
                curr = 0
                head = i    # move head to current position
            else:
                curr = i - head
                total += curr

        return total
