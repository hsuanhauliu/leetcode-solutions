from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = Counter(t)   # all counts of elements in t
        missing = len(t)    # remaining letters needed in substring
        letters = set(t)    # all unique letters in t
        last_head_pos = len(s) - len(t) + 1

        head = tail = 0     # pointers for start and end of the substring
        curr_length = len(s) + 1
        shortest_str = ""   # current shortest substring
        while head < last_head_pos:
            if missing:
                if tail == len(s):
                    break
                if s[tail] in letters:
                    if need[s[tail]] > 0:
                        missing -= 1
                    need[s[tail]] -= 1
                tail += 1
            else:
                if tail - head < curr_length:
                    curr_length = tail - head
                    shortest_str = s[head:tail]
                if s[head] in letters:
                    need[s[head]] += 1
                    if need[s[head]] > 0:
                        missing += 1
                head += 1

        return shortest_str
