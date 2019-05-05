class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        sorted_people = sorted(people)
        h = 0
        t = len(people) - 1
        boat_count = 0
        
        while h <= t:
            if h != t and sorted_people[h] <= limit - sorted_people[t]:
                h += 1
            t -= 1
            boat_count += 1
        return boat_count