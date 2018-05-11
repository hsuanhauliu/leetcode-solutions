class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        returnStr = ""
        difference = 2 * (numRows - 1)
        if numRows == 1:
            difference = 1
        length = len(s)

        for i in xrange(numRows):
            compliment = difference - 2 * i
            current_position = i

            while current_position < length:
                returnStr += s[current_position]
                if i != 0 and i != (numRows - 1) and (current_position + compliment) < length:
                    returnStr += s[current_position + compliment]
                current_position += difference
                
        return returnStr
