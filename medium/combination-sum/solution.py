class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_c = sorted(candidates, reverse=True)
        res = set()
        self.find_comb(target, sorted_c, [], res)
        return [sorted(tu) for tu in res]
        
    def find_comb(self, t, nums, curr_c, all_comb):
        if not t:
            all_comb.add(tuple(sorted(curr_c)))
            return
        
        for n in nums:
            if n <= t:
                self.find_comb(t - n, nums, curr_c + [n], all_comb)