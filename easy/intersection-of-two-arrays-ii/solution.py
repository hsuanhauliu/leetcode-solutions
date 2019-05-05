class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        p_1 = p_2 = 0
        
        while p_1 < len(nums1) and p_2 < len(nums2):
            if sorted_nums1[p_1] == sorted_nums2[p_2]:
                res.append(sorted_nums1[p_1])
                p_1 += 1
                p_2 += 1
            elif sorted_nums1[p_1] < sorted_nums2[p_2]:
                p_1 += 1
            else:
                p_2 += 1
        return res