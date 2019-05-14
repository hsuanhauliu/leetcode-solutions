class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        if length != len(t):
            return False
        
        mapping = {}
        added = set()
        for i in range(length):
            if s[i] not in mapping.keys():
                if t[i] not in added:
                    mapping[s[i]] = t[i]
                    added.add(t[i])
                else:
                    return False
            elif mapping[s[i]] != t[i]:
                return False
        return True
