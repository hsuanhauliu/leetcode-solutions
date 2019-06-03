class TimeMap:
    """ A simple implementation using a dictionary of lists of tuples.
    Check latest time stamp to avoid unnecessary lookup.
    
    Time:
        set: O(1)
        get: O(n)
        
    Space: O(n)
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_map = {}
        self.curr_time = 0

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key].insert(0, (value, timestamp))
        else:
            self.time_map[key] = [(value, timestamp)]
        curr_time = timestamp

    def get(self, key: str, timestamp: int) -> str:
        if timestamp >= self.curr_time and key in self.time_map and self.time_map[key]:
            values = self.time_map[key]
            if values[-1][1] <= timestamp:
                for v, t in values:
                    if t <= timestamp:
                        return v
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)