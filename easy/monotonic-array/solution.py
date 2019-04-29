class Solution(object):
    def isMonotonic(self, a):
        """
        :type A: List[int]
        :rtype: bool
        """
        incre, decre = True, True
        for i in range(1, len(a)):
            if a[i - 1] < a[i]:
                decre = False
            elif a[i - 1] > a[i]:
                incre = False
        return incre or decre
