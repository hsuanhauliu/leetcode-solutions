from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letters = Counter(map(lambda l: l.lower(), filter(lambda l: l.isalpha(), licensePlate)))
        return min([w for w in words if Counter(w) & letters == letters], key=len)
