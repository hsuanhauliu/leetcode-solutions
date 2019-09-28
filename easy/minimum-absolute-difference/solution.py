class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)

        # first find minimum difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, sorted_arr[i] - sorted_arr[i-1])

        # find every pair with the min_diff
        return [[sorted_arr[i-1], sorted_arr[i]] for i in range(1, len(sorted_arr)) if sorted_arr[i] - sorted_arr[i-1] == min_diff]
            
