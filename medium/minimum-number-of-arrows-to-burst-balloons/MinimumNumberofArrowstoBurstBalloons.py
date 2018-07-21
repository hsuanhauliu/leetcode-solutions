from operator import itemgetter

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        sortedList = sorted(points, key=itemgetter(1))
        arrowList = [sortedList[0][1]]

        for b in range(1, len(sortedList)):
            if sortedList[b][0] > arrowList[-1]:
                arrowList.append(sortedList[b][1])

        return len(arrowList)