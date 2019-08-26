class Solution:
    def advantageCount(self, a: List[int], b: List[int]) -> List[int]:
        size = len(a)
        a.sort(reverse=True)
        b_c = sorted([(v, i) for i, v in enumerate(b)], reverse=True)
        a_i = b_i = 0
        res = [-1] * size
        while b_i < size:
            if a[a_i] > b_c[b_i][0]:
                res[b_c[b_i][1]] = a[a_i]
                a_i += 1
            b_i += 1
        
        for i, num in enumerate(res):
            if num == -1:
                res[i] = a[a_i]
                a_i += 1
        return res