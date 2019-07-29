from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """ Make two lists to keep track of elements that are in arr2 and aren't.
        Sort the list that contain elements that aren't in arr2 and combine.
        Time: O(nlogn)
        Space: O(n)
        """
        counts = Counter(arr1)
        nums = set(arr2)
        res = []
        remain = []
        for num, count in counts.items():
            if num not in nums:
                for _ in range(count):
                    remain.append(num)
        remain.sort()
        
        for num in arr2:
            for _ in range(counts[num]):
                res.append(num)
        return res + remain