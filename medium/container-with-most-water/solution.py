class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        head = 0
        tail = len(height) - 1

        while head < tail:
            curr_area = min(height[head], height[tail]) * (tail - head)
            if curr_area > max_area:
                max_area = curr_area

            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1

        return max_area
