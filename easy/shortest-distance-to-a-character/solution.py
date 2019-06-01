class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        """
        Find pairs of character c and calculate the distance in between.
        
        Time: O(n)
        Space: O(n)
        """
        res = [0] * len(s)
        char_index = [i for i in range(len(s)) if s[i] == c]
                
        # iterate through each pair of zeros
        for i in range(1, len(char_index)):
            head = char_index[i - 1] + 1
            tail = char_index[i] - 1
            counter = 1
            while head <= tail:
                res[head] = res[tail] = counter
                counter += 1
                head += 1
                tail -= 1
        
        # fill out both sides
        counter = 1
        left = char_index[0] - 1
        while left >= 0:
            res[left] = counter
            counter += 1
            left -= 1
        
        counter = 1
        right = char_index[-1] + 1
        while right < len(s):
            res[right] = counter
            counter += 1
            right += 1
        
        return res
                