class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        newS = ""
        if len(S) == 0:
            return newS

        total = 0
        for n in shifts:
            total += n

        for i in xrange(len(S)):
            newS += self.shift(S[i], total)
            total -= shifts[i]

        return newS
                        
    def shift(self, ch, num):
        new = ord(ch) + (num % 26)
        if new > 122:
            new -= 26

        return chr(new)

