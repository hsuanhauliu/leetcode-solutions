class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        s_size = len(s)
        t_size = len(t)
        if t_size < s_size:
            return False
        if not s:
            return True
        
        for t_letter in t:
            if t_letter == s[s_index]:
                s_index += 1
            if s_index == s_size:
                return True
        
        return False