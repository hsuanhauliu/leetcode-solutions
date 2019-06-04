from bisect import bisect_left

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """ DP solution
        Sort and eliminate tasks with same difficulty but lower profit as we will never
        choose them. Use a dp list to memorize the most profits that one can make on
        tasks that are equal or lower to the task at that index. Finally, simply use
        a binary search to find the highest difficulty task that is lower than or equal
        to the capability of the worker.
        
        Time: O(nlogn)
        Space: O(n)
        """
        jobs = sorted(zip(difficulty, profit), key=lambda x: (x[0], x[1]))
        
        # eliminate duplicates
        prev = None
        for i in reversed(range(len(difficulty))):
            if prev == jobs[i][0]:
                jobs.pop(i)
            else:
                prev = jobs[i][0]
        
        # go through all tasks to find most profit one can make at each difficulty
        n = len(jobs)
        tasks, dp = list(zip(*jobs))
        dp = list(dp)
        for i in range(1, n):
            dp[i] = max(jobs[i][1], dp[i-1])
        
        total_profit = 0
        for capability in worker:
            pos = bisect_left(tasks, capability)
            if pos == n or tasks[pos] > capability:
                pos -= 1
            if pos >= 0:
                total_profit += dp[pos]
        
        return total_profit