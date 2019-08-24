class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """ Recursively maximize player 1's score with memoization.
        
        Time: O(n^2)
        Space: O(n^2)
        """
        size = len(nums)
        if size < 3:
            return True
        
        memo = [[-1] * size for _ in range(size)]
        my_score = self.calc_score(nums, 0, size - 1, memo)
        return 2 * my_score >= sum(nums)
    
    
    def calc_score(self, nums, i, j, lookup):
        if i == j:
            return nums[i]
        
        if i > j:
            return 0
        
        if lookup[i][j] == -1:
            lookup[i][j] = max(nums[i] + min(self.calc_score(nums, i+2, j, lookup),
                                             self.calc_score(nums, i+1, j-1, lookup)),
                               nums[j] + min(self.calc_score(nums, i, j-2, lookup),
                                             self.calc_score(nums, i+1, j-1, lookup)))
        return lookup[i][j]