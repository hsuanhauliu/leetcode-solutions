class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        new_trips = self.break_trips(trips)
        curr_num = 0
        for loc, num_p in new_trips:
            curr_num += num_p
            if curr_num > capacity:
                return False
            
        return True
    
    
    def break_trips(self, trips):
        res = []
        for num_p, start, end in trips:
            res.append((start, num_p))
            res.append((end, -num_p))
        res.sort()
        return res