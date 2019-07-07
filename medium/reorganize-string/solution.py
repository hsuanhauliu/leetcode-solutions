import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = []
        counts = Counter(s)
        for l, c in counts.items():
            heapq.heappush(letters, (-c, l))
        
        res = ""
        prev_c, prev_l = 0, ""
        while letters:
            curr_c, curr_l = heapq.heappop(letters)
            res += curr_l
            curr_c += 1
            if prev_c:
                heapq.heappush(letters, (prev_c, prev_l))
                
            prev_c = curr_c
            prev_l = curr_l
        
        return res if len(res) == len(s) else ""