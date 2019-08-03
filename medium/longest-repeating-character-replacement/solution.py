class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """ Sliding window approach.
        The idea is to keep a window size that can store the longest
        substring and keep track of the letter with the highest frequency
        we've seen. The window size cannot grow beyond the size allowed,
        which is the size of the substring - maximum frequency of a letter
        in the longest substring.
        
        Time: O(n)
        Space: O(1) there can be at most 26 characters.
        """
        curr_max, start, size = 0, 0, len(s)
        counts = {}
        for tail in range(size):
            char = s[tail]
            counts[char] = counts.get(char, 0) + 1
            curr_max = max(curr_max, counts[char])
            if tail - start - curr_max + 1 > k:
                counts[s[start]] -= 1
                start += 1
        return size - start