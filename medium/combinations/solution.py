class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        if k <= n:
            self.find_comb(1, k, n, [], res)
        return res
    
    
    def find_comb(self, curr, k, n, seq, res):
        if not k:
            res.append(seq)
            return
        
        for i in range(curr, n - k + 2):
            self.find_comb(i + 1, k - 1, n, seq + [i], res)