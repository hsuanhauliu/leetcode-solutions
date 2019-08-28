from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        """ Sliding Window approach. Expand only if all characteres are the same
        or if we can swap the character that is different from the rest.
        
        Time: O(n^2)    bottleneck: how we find the most frequent character in the
                        current window. Can probably keep track of it somehow...
        Space: O(n)
        """
        size = len(text)
        total = Counter(text)
        p_1 = 0 # start of the sliding window
        curr_counts = {}
        
        for p_2, char in enumerate(text):
            curr_counts[char] = curr_counts.get(char, 0) + 1
            max_char, char_count = self.find_most_freq(curr_counts)
            window_size = p_2 - p_1 + 1
            if window_size > char_count and (total[max_char] == char_count or window_size > char_count + 1):
                curr_counts[text[p_1]] -= 1
                p_1 += 1
        
        return size - p_1
    
    
    def find_most_freq(self, counts):
        max_char, char_count = '', 0
        for char, counts in counts.items():
            if counts > char_count:
                max_char, char_count = char, counts
        return max_char, char_count