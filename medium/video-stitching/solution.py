class Solution:
    def videoStitching(self, clips: List[List[int]], t: int) -> int:
        """ Greedy approach.
        Keep choosing the overlapping clip that will take us furtherest.
        
        Time: O(nlogn)
        Space: O(n)
        """
        n = len(clips)
        sorted_clips = sorted(clips, key=lambda x: (x[0], -x[1]))
        curr_pos = curr_next = counter = i = 0
        
        while curr_pos < t and i < n :
            start, end = sorted_clips[i]
            # overlaps
            if start <= curr_pos:
                curr_next = max(curr_next, end)
                i += 1
            elif curr_pos != curr_next:
                curr_pos = curr_next
                counter += 1
            else:
                return -1
            
            # if reached
            if curr_next >= t:
                counter += 1
                curr_pos = curr_next
            
        return -1 if curr_pos < t else counter