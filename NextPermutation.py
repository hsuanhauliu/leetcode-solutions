class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # do not change if the number is one digit or less
        length = len(nums)
        if length < 2:
            return

        # test if the number is in descending order
        if self.is_descending(nums):
            self.convert_ascending(nums)
            return

        # find next permutation
        for j in reversed(range(length - 1)):
            for i in reversed(range(j, length)):
                if nums[i] > nums[j]:
                    # do a swap
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp

                    # sort the remaining list
                    nums[j+1:] = sorted(nums[j+1:])
                    
                    return

        return

    def is_descending(self, numbers):
        for i in range(1, len(numbers)):
            if numbers[i - 1] < numbers[i]:
                return False

        return True

    def convert_ascending(self, numbers):
        length = len(numbers)

        for i in xrange(length / 2):
            temp = numbers[i]
            numbers[i] = numbers[length - 1 - i]
            numbers[length - 1 - i] = temp

        return
