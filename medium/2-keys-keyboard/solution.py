class Solution:
    def minSteps(self, n: int) -> int:
        """ BFS """
        if n == 1:
            return 0
        if n == 2:
            return 2
        
        checked = set()
        checked.add((2, 1))
        res = 2
        curr_q = [(2, 1)]
        while curr_q:
            res += 1
            next_q = []
            for curr_n, copied in curr_q:
                if curr_n != copied and (curr_n, curr_n) not in checked:
                    next_q.append((curr_n, curr_n))
                    checked.add((curr_n, curr_n))
                    
                next_n = curr_n + copied
                if next_n == n:
                    return res
                if next_n < n and (next_n, copied) not in checked:
                    next_q.append((next_n, copied))
                    checked.add((next_n, copied))
            curr_q = next_q