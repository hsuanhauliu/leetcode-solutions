from collections import Counter

class Solution:
    def canReorderDoubled(self, a: List[int]) -> bool:
        counts = Counter(a)
        for num in sorted(a):
            if counts[num]:
                next_num = 0
                if num > 0:
                    next_num = 2 * num
                else:
                    next_num = num / 2
                if next_num in counts and counts[next_num]:
                    counts[num] -= 1
                    counts[next_num] -= 1
                else:
                    return False
        
        return True