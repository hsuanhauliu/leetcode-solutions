class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # base case
        if n <= 0:
            return False

        while n != 1:
            if n % 3 != 0:
                return False
            n //= 3

        return True

def main():
    sol = Solution()
    print(sol.isPowerOfThree(10) == False)
    print(sol.isPowerOfThree(9) == True)
    print(sol.isPowerOfThree(81) == True)
    print(sol.isPowerOfThree(0) == False)
    print(sol.isPowerOfThree(-27) == False)
    print(sol.isPowerOfThree(-25) == False)


if __name__ == "__main__":
    main()
