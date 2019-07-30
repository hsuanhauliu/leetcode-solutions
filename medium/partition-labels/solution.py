class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """ Two pass approach
        Time: O(n)
        Space: O(1) because result can at most be of size 26 (num of letters)
        """
        # find last position of each character
        last_pos = {char: i for i, char in enumerate(s)}
        
        size = len(s)
        par_len = 0
        par_last_pos = 0
        res = []
        for i in range(size):
            if i > par_last_pos:
                res.append(par_len)
                par_len = 1
                par_last_pos = last_pos[s[i]]
            else:
                par_len += 1
                par_last_pos = max(par_last_pos, last_pos[s[i]])
        res.append(par_len)
        return res