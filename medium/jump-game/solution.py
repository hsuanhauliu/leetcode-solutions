class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furtherest_pos = 0

        for curr_pos in range(len(nums)):
            if curr_pos > furtherest_pos:
                return False
            furtherest_pos = max(curr_pos + nums[curr_pos], furtherest_pos)
        return True


def main():
    sol = Solution()

    # normal cases
    print(sol.canJump([0, 0, 0, 0, 0, 0]) == False)
    print(sol.canJump([2, 3, 1, 1, 4]) == True)
    print(sol.canJump([3, 2, 1, 0, 4]) == False)

    # edge cases
    print(sol.canJump([]) == True)
    print(sol.canJump([0]) == True)


if __name__ == '__main__':
    main()
