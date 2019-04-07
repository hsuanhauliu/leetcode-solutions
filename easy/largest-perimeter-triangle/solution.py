class Solution(object):
    def largestPerimeter(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        a.sort(reverse=True)
        for n in range(2, len(a)):
            if a[n - 2] < a[n - 1] + a[n]:
                return a[n - 2] + a[n - 1] + a[n]
        return 0


def main():
    sol = Solution()
    print(sol.largestPerimeter([]) == 0)
    print(sol.largestPerimeter([1, 2]) == 0)
    print(sol.largestPerimeter([1, 1, 2]) == 0)
    print(sol.largestPerimeter([1, 2, 2]) == 5)
    print(sol.largestPerimeter([3, 2, 3, 4]) == 10)
    print(sol.largestPerimeter([3, 6, 2, 3]) == 8)


if __name__ == "__main__":
    main()
