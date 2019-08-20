class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        
        if sum(nums) % k:
            return False
        
        self.nums = sorted(nums, reverse=True)
        self.target = sum(nums) // k
        self.size = len(nums)
        self.visited = [False] * self.size
        return self.dfs(k, self.target, 0)
    
    
    def dfs(self, k, remain, curr):
        if not k:
            return True
        
        if not remain:
            return self.dfs(k-1, self.target, 0)
        
        for i in range(curr, self.size):
            n = self.nums[i]
            if not self.visited[i] and n <= remain:
                self.visited[i] = True
                if self.dfs(k, remain-n, i+1):
                    return True
                self.visited[i] = False
        return False