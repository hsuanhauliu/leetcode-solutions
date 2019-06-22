from collections import Counter

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """ Count number of aligned edges
        Use the total number of layers minus the number of aligned edges.
        
        Time: O(n)
        Space: O(n)
        where n is the number of ints in the input.
        """
        n = len(wall)
        gaps = []
        for i in range(n):
            curr_sum = 0
            for j in range(len(wall[i]) - 1):
                curr_sum += wall[i][j]
                gaps.append(curr_sum)
        
        gaps = Counter(gaps)
        maximum = max(val for _, val in gaps.items())
            
        return n - maximum