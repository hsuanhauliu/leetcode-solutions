class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def checkPalindrome(s, deleted):
            head = 0
            tail = len(s) - 1
            
            while head < tail:
                if s[head] != s[tail]:
                    if deleted:
                        return False
                    else:
                        return checkPalindrome(s[head+1:tail+1], True) or\
                               checkPalindrome(s[head:tail], True)
                head += 1
                tail -= 1

            return True

        return checkPalindrome(s, False)
