from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        return c1 & c2 == c1