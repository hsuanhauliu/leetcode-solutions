class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        MAX = 1440
        
        # convert clock time to minutes
        timePoints = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timePoints])
        
        diff = timePoints[-1] - timePoints[0]
        minimum = min(diff, MAX - diff)
        
        for i in range(1, len(timePoints)):
            diff = timePoints[i] - timePoints[i-1]
            minimum = min(minimum, diff)
        
        return minimum