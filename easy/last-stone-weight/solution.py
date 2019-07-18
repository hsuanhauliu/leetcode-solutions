import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inversed = [-x for x in stones]
        heapq.heapify(inversed)
        while len(inversed) > 1:
            first = heapq.heappop(inversed)
            second = heapq.heappop(inversed)
            diff = first - second
            if diff:
                heapq.heappush(inversed, diff)
        
        return -inversed[0] if inversed else 0