from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """ Greedy solution
        Grab the most frequent and also available task.
        Time: O(N * n); where N is the tasks and n in the wait time
        Space: O(1); the number of tasks can only be at most 26 (capital letters)
        
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        def fix_order(l, pos):
            for i in range(pos, len(l) - 1):
                if l[i][1] < l[i+1][1]:
                    temp = l[i]
                    l[i] = l[i+1]
                    l[i+1] = temp
                else:
                    return
                
        intervals = 0
        remaining = len(tasks)
        order = [[t, num, 1] for t, num in Counter(tasks).most_common()]
        while remaining:
            intervals += 1
            # see which task we can do next
            for i in range(len(order)):
                # if no task is available
                if not order[i][1]:
                    break
                
                # if we found a task to assign
                if order[i][2] <= intervals:
                    order[i][1] -= 1
                    order[i][2] = intervals + n + 1
                    remaining -= 1
                    fix_order(order, i)
                    break
                    
        return intervals