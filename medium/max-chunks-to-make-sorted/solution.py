class Solution:
    def maxChunksToSorted(self, arr):
        tasks = [(i, v) if i < v else (v, i) for i, v in enumerate(arr)]
        tasks.sort()
        
        i = 0
        while i < len(tasks) - 1:
            curr_t = tasks[i]
            next_t = tasks[i + 1]

            # merge
            if next_t[0] <= curr_t[1]:
                tasks.pop(i + 1)
                tasks[i] = (curr_t[0], max(curr_t[1], next_t[1]))
            else:
                i += 1
        
        return len(tasks)
