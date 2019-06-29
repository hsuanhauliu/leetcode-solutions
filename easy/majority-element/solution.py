from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        counts = Counter(nums)
        for num, count in counts.items():
            if count > threshold:
                return num
        return