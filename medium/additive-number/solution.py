class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        size_a, size_b, size_num = 1, 1, len(num)
        if size_num < 3:
            return False
        
        while max(size_a, size_b) * 2 <= size_num:
            a, b = num[:size_a], num[size_a: size_a + size_b]
            if size_a > 1 and a[0] == '0':
                return False
            if size_b > 1 and b[0] == '0':
                size_a += 1
                size_b = 1
                continue
                
            remaining = num[size_a + size_b:]
            while remaining:
                c = str(int(a) + int(b))
                size_c = len(c)
                if len(remaining) < size_c:
                    break
                
                next_num = remaining[:size_c]
                remaining = remaining[size_c:]
                if c != next_num:
                    break
                elif not remaining:
                    return True
                else:
                    a, b = b, c
            size_b += 1
            if max(size_a, size_b) * 2 > size_num:
                size_a += 1
                size_b = 1
                
        return False