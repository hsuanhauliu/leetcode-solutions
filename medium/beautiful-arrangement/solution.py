class Solution(object):
    def countArrangement(self, n):
        """
        :type N: int
        :rtype: int
        """
        return self.test_combination(n, set(range(1, n + 1)))

    def test_combination(self, pos, remaining):
        if pos == 1:
            return 1

        total = 0
        for num in remaining:
            if num % pos == 0 or pos % num == 0:
                total += self.test_combination(pos - 1, remaining - {num})
        return total
