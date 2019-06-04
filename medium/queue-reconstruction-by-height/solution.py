class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_copy = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for v in people_copy:
            res.insert(v[1], v)
        
        return res