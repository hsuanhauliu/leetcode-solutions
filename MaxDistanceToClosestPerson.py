class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        leftPerson = 0
        rightPerson = 0
        middle = 0
        maxDist = 0

        for i in xrange(len(seats)):
            if seats[i] == 1:
                leftPerson = i
                break
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                rightPerson = i
                break

        count = 0
        for i in range(leftPerson+1, rightPerson+1):
            if seats[i] == 0:
                count += 1
            else:
                if count != 0:
                    if maxDist < count + 1:
                        maxDist = count + 1
                    count = 0

        maxDist /= 2
        if maxDist < leftPerson:
            maxDist = leftPerson

        if maxDist < (len(seats) - 1 - rightPerson):
            maxDist = len(seats) - 1 - rightPerson

        return maxDist
