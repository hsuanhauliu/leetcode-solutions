class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        size = len(pattern)
        if size != len(words):
            return False
        
        mapping, inverse_mapping = {}, {}
        for i in range(size):
            p, word = pattern[i], words[i]
            
            if p in mapping and word in inverse_mapping:
                if mapping[p] != word or inverse_mapping[word] != p:
                    return False
            elif p not in mapping and word not in inverse_mapping:
                mapping[p] = word
                inverse_mapping[word] = p
            else:
                return False
        
        return True