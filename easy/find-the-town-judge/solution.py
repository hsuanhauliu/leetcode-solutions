class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        # find the person that trusts no one: O(n)
        everyone = set(person for person in range(1, n + 1))
        p_a = set(person[0] for person in trust)
        candidates = everyone - p_a
        
        # count number of people who trust the candidates O(n)
        counts = {}
        for a, b in trust:
            if b in candidates:
                counts[b] = counts.get(b, 0) + 1
                if counts[b] == n - 1:
                    return b
        return -1