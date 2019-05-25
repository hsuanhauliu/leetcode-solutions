class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_1, candidate_2 = 0, 1
        votes_1, votes_2 = 0, 0
        for n in nums:
            if n == candidate_1:
                votes_1 += 1
            elif n == candidate_2:
                votes_2 += 1
            elif votes_1 == 0:
                candidate_1, votes_1 = n, 1
            elif votes_2 == 0:
                candidate_2, votes_2 = n, 1
            else:
                votes_1 -= 1
                votes_2 -= 1
                
        # check if they actually appear more than n/3 times
        res = []
        votes_1 = votes_2 = 0
        for n in nums:
            if n == candidate_1:
                votes_1 += 1
            elif n == candidate_2:
                votes_2 += 1
        
        if votes_1 > len(nums) / 3:
            res.append(candidate_1)
        if votes_2 > len(nums) / 3:
            res.append(candidate_2)
            
        return res