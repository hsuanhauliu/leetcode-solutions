class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        def isValid(w):
            pointer_w = 0
            for char in s:
                if char == w[pointer_w]:
                    pointer_w += 1
                    if pointer_w == len(w):
                        return True
                    
            return False
            
        longest_word = ""
        for word in sorted(d):
            if isValid(word) and len(word) > len(longest_word):
                longest_word = word
                
        return longest_word