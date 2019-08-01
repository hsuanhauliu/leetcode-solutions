class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ Bi-directional search """
        if endWord not in wordList:
            return 0
        
        words = set(wordList)
        counter = 0
        curr_q_1 = set([beginWord])
        curr_q_2 = set([endWord])
        visited = set()
        while curr_q_1 and curr_q_2:
            counter += 1
            next_q_1, next_q_2 = set(), set()
            for curr_w in curr_q_1:
                visited.add(curr_w)
                if curr_w in curr_q_2:
                    return counter * 2 - 1
                for neighbor in self._get_neighbors(curr_w, words):
                    if neighbor not in visited:
                        next_q_1.add(neighbor)
            
            for curr_w in curr_q_2:
                visited.add(curr_w)
                if curr_w in next_q_1:
                    return counter * 2
                for neighbor in self._get_neighbors(curr_w, words):
                    if neighbor not in visited:
                        next_q_2.add(neighbor)
            curr_q_1, curr_q_2 = next_q_1, next_q_2
        return 0
    
    
    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """ Simple BFS """
        if endWord not in wordList:
            return 0
        
        words = set(wordList)
        curr_q = [beginWord]
        visited = set()
        counter = 1
        while curr_q:
            counter += 1
            next_q = []
            for curr_w in curr_q:
                visited.add(curr_w)
                neighbors = self._get_neighbors(curr_w, words)
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return counter
                    if neighbor not in visited:
                        next_q.append(neighbor)
            curr_q = next_q
        return 0
    
    def _get_neighbors(self, curr_w, words):
        res = []
        for i in range(len(curr_w)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_w = curr_w[:i] + c + curr_w[i+1:]
                if new_w in words:
                    res.append(new_w)
        return res
    