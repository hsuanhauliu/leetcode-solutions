class Solution:
    def numSquares(self, n: int) -> int:
        """ BFS
        Time: O(n ^ (3/2))
        Space: O(n)
        """
        curr_q = [n]
        checked = set([n])
        depth = 0
        while curr_q:
            depth += 1
            next_q = []
            for num in curr_q:
                for path in range(1, int(num ** (1/2)) + 1):
                    remain = num - (path ** 2)
                    if not remain:
                        return depth
                    
                    if remain not in checked:
                        next_q.append(remain)
                        checked.add(remain)
            curr_q = next_q