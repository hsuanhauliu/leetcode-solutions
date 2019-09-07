from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = b = 0
        for i in range(min(len(secret), len(guess))):
            a += 1 if secret[-i - 1] == guess[-i - 1] else 0
        
        count_s, count_g = Counter(secret), Counter(guess)
        for num in '0123456789':
            b += min(count_s[num], count_g[num])
        
        return str(a) + 'A' + str(b - a) + 'B'