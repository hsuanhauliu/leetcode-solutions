class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype List[List[int]]
        """
        if len(nums) == 0:
            return []
        
        return_list = []
        count_dict = {}
        count_list = []

        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1
        for k, c in count_dict.items():
            count_list.append([k, c])

        self.findSubSet(return_list, [], count_list)
        return return_list

    def findSubSet(self, return_list, curr_list, remaining):
        return_list.append(curr_list)

        for i in range(len(remaining)):
            sub_curr = curr_list[:]
            sub_curr.append(remaining[i][0])

            if remaining[i][1] != 1:
                subset = [l[:] for l in remaining[i:]]
                subset[0][1] -= 1
                self.findSubSet(return_list, sub_curr, subset)
            else:
                self.findSubSet(return_list, sub_curr, remaining[i+1:])


sol = Solution()
print(sol.subsetsWithDup([]))
