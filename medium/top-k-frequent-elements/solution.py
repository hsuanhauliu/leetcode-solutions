from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ Keep a min-heap of size m, where m is the number of unique
        elements.
        
        Time: O(mlogk)
        Space: O(m)
        """
        counts = Counter(nums)
        elements = []
        for num, count in counts.items():
            if len(elements) < k:
                heapq.heappush(elements, (count, num))
            elif elements[0][0] < count:
                heapq.heappop(elements)
                heapq.heappush(elements, (count, num))
        return [num for _, num in elements]
    
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """ Use min-heap to pop m-k elements to return the remaining elements,
        where m is the number of unique elements in nums list. n is the total
        number of elements in nums.
        
        Time: O(mlogm) because forming the heap is the bottleneck.
        Space: O(m)
        """
        counts = Counter(nums)
        elements = []
        for num, count in counts.items():
            heapq.heappush(elements, (count, num))
        
        for _ in range(len(counts) - k):
            heapq.heappop(elements)
        
        return [num for _, num in elements]