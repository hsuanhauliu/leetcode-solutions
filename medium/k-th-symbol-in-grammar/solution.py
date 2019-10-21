class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """ Track if the current node is the same as parent node.
        
            Time: O(n)
            Space: O(1)
        """
        same = True
        for _ in range(n - 1):
            if not k % 2:
                same = not same
                k /= 2
            else:
                k = (k + 1) / 2
        return 0 if same else 1

    def kthGrammar2(self, n: int, k: int) -> int:
        """
            Backtrack from nth row to root to find the path. This way
            we don't have to unnecessarily find all numbers for every
            row.
            
            Time: O(n)
            Space: O(n)
        """
        moves, k = [False] * (n - 1), k - 1
        for i in range(n - 1):
            moves[i] = bool(k % 2)
            k //= 2
        
        res = False
        for right_branch in moves[::-1]:
            res ^= right_branch
        
        return 1 if res else 0