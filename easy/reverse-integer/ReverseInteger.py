class Solution(object):
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        mylist = [c for c in reversed(str(x))]
        mystr = ''.join(mylist)
        result = int(mystr)

        if (result >> 31) != 0:
            return 0

        return sign * result
