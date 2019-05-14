class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        if p1
        def cal_dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        sides = []
        p = [p1, p2, p3, p4]
        for i in range(4):
            sides.append(cal_dist(p[i-1], p[i]))

        sides.append(cal_dist(p1, p3))
        sides.append(cal_dist(p2, p4))
        sides.sort()

        return sides[0] == sides[1] == sides[2] == sides[3] and sides[4] == sides[5]
