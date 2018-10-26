class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        my_N = N
        prev = None
        curr_num = 0
        highest = 0
        counter = 0
        changed = False

        while my_N != 0:
            curr = my_N % 10
            my_N //= 10

            if prev != None and curr > prev:
                highest = counter
                curr_num = curr
                changed = True
            elif prev != None and curr == prev and curr == curr_num:
                highest = counter

            prev = curr
            counter += 1

        if changed:
            power = 10 ** highest
            return N - N % (power * 10) + (power * curr_num) - 1

        return N
