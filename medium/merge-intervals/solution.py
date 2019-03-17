# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        results = []

        for i in sorted(intervals, key=lambda i: i.start):
            if results and i.start <= results[-1].end:
                results[-1].end = max(results[-1].end, i.end)
            else:
                results.append(i)
        return results
