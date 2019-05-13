class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = []
        for x, y in points:
            distances.append((x ** 2 + y ** 2, x, y))

        return [[x, y] for _, x, y in sorted(distances)[:K]]
