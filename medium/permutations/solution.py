class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        all_permutations = []
        size = len(nums)
        self.find_p_recursive(nums, all_permutations, [0] * size, 0)

        return all_permutations

    def find_p_recursive(self, nums, a, curr, curr_i):
        if not nums:
            a.append(curr)
            return

        curr_dup = curr[:]
        for i in range(len(nums)):
            curr_dup[curr_i] = nums[i]
            self.find_p_recursive(nums[:i] + nums[i + 1:], a, curr_dup, curr_i + 1)
